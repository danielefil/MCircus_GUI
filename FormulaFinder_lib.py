import re
import pandas as pd
import numpy as np
#from pandas.core.indexes.base import Index

### DBE CALCULATOR ###
def DBE(formula):
    l = dict(re.findall("(\D+)(\d+)", formula))
    def m(k): return int(l.get(k, 0))
    return(m("C") and m("C")+1+(m("N")-sum(map(m, "F I H Cl Br".split())))/2)

### NEW MASS CALCULATOR ###
def delta_ppm_converter(mass, ppm):
    _delta = (mass * ppm / 1000000)
    return _delta

### ppm CALCULATOR ###
def ppm_calc(m1, m2):
    _ppm = round(abs((m1-m2)*1000000/m1), 2)
    return _ppm

### RATIOS CALCULATOR ###
def ratio_calc(formula, atom):
    l = dict(re.findall("(\D+)(\d+)", formula))
    ratios = int(l.get(atom, 0))/int(l.get("C", 0))
    return ratios

def carbon(formula):
    c = dict(re.findall("(\D+)(\d+)", formula))
    _carbon = c.get("C", 0)
    return (_carbon)

### CLEANER - Rimuove gli atomi con pedice 0 -
def cleaner(formula):
    parsed = re.findall(r"([A-Z][a-z]*)(\d*)|(\()|(\))(\d*)", formula)
    cleand_formula = ""
    for element_details in parsed:
        element = element_details[0]
        element_count = element_details[1]
        if element_count != "0":
            cleand_formula = cleand_formula + element + element_count
    if cleand_formula != "":
        return cleand_formula
    else:
        return None

### DECOMPOSER ###
def decomposer(Mtot, atoms, limits, mass=0, formula="", output=[]):
    if atoms != []:
        if Mtot >= atoms[0][1]:
            Nmax = int(min(atoms[0][3], (Mtot)//atoms[0][1]))
            Nmin = atoms[0][2]
            if len(atoms) == 1: # Se ultimo atomo correggo Nmin
                Nmin = int(max(atoms[0][2], (Mtot)//atoms[0][1]))
            for A in list(range(Nmin, Nmax+1)):
                NewMtot = Mtot - A*atoms[0][1]
                Newmass = mass + A*atoms[0][1]
                NewFormula = formula + str(atoms[0][0])+str(A)
                NewAtom = atoms[1:]
                if limits[0] < Newmass < limits[1]:
                    output.append((str(NewFormula), round(Newmass,5)))
                decomposer(NewMtot, NewAtom, limits, Newmass, NewFormula, output)

        else:
            atoms = atoms[1:]
            decomposer(Mtot, atoms, limits, mass, formula, output)
    
    return output    


def FormulaFinder(spectrum_path, atoms, charge, ppm, out):
    df_sp = pd.read_csv(spectrum_path, dtype={"Mass [m/z]": float, "Intensity": float})
    spectra = np.round(df_sp.to_numpy(), 5)
    spectra = df_sp.to_numpy()
    
    for values in spectra:
        output = []
        delta = delta_ppm_converter(values[0], ppm)
        # Inizzate 
        Mass_to_find = values[0] - (charge * 0.00054387)
        
        # Protonate o deprotonate
        # Mass_to_find = values[0] -(charge*1.0072764)  
        
        limits = [Mass_to_find-delta, Mass_to_find+delta]
        Formulas = decomposer(limits[1], atoms, limits, 0, output=output)
        if len(Formulas) != 0:
            for iii in Formulas:
                out.append([values[0], values[1], iii[0], iii[1]])
        
    df_output = pd.DataFrame(out, columns=["m/z", "Intensity" , "Formula", "Neutral Mass"])
    return(df_output)
    


def FormulaRefiner(Compounds_path, charge: int, filtri: dict):
    df_results = pd.read_csv(Compounds_path, dtype={"m/z": float, "Intensity": float , "Formula": str, "Neutral Mass": float})
    newname = Compounds_path.replace(".csv","_CompoundList.csv") 
    # Controlo che il file dei composti da cercare non sia vuoto
    if len(df_results) == 0:
        # NO, rise Error
        print("Zero")
        df_results.to_csv(newname)
    else:
        # OK, posso usare il file
        # pulisco le formule
        print("OK")
        df_results["Formula"] = df_results["Formula"].apply(cleaner)
        
        
        ## pulisco le formule senza carbonio
        df_results = df_results.drop(df_results[df_results["Formula"].apply(carbon) == 0].index)

        ## calcolo la differenza in ppm
        #FOR M+ and M-
        adduct_corr = charge*0.00054387
        df_results["ppm"] = df_results.apply(lambda x: ppm_calc(x["m/z"], (x["Neutral Mass"]-adduct_corr)), axis=1)

        #FOR PROTONATION ADN DEPROTONATION
        #adduct_corr = charge*1.0072764
        #df_results["ppm"] = df_results.apply(lambda x: ppm_calc(x["m/z"], (x["Neutral Mass"]+adduct_corr)), axis=1)

        for key, values in filtri.items():
            if key == "DBE":
                ## calcolo DBE
                df_results[key] = df_results["Formula"].apply(DBE)
                df_results = df_results[(df_results[key] >= values[0]) & (df_results[key] <= values[1])]
            else:
                df_results[key + "/C"] = df_results.apply(lambda x: ratio_calc(x["Formula"], key), axis=1)
                df_results = df_results[(df_results[key + "/C"] >= values[0]) & (df_results[key + "/C"] <= values[1])]
            
            if len(df_results) == 0:
                break
    
    df_results2 = df_results[["Formula", "m/z"]]
    df_results2.to_csv(newname, index=False)
    return(newname)
        

######################################
###########  MAIN PROGRAM  ###########
######################################




## WIN PATH
#spectrum_path = r"C:\Users\df426\Desktop\AnalisiCromo\Spectra\Part2_2020_7_3_cromoacetato_gallico_1a3_h2o_meoh_1a100_400-2000_NEG.csv"
#atoms = [["Cr", 51.9405119, 1, 3], ["O", 15.9949146221, 1, 50], ["C", 12.0, 1, 50], ["H", 1.00783, 1, 10]]
#out = []
#c = FormulaFinder(spectrum_path,atoms, -1, 10, out)
#c.to_csv(r"C:\Users\df426\Desktop\AnalisiCromo\Spectra\tt.csv", index=False)

# lista contenete gli atomi sui quali voglio calcolare i rapporti con il carbonio
#spectrum_path = r"C:\Users\df426\Desktop\AnalisiCromo\Spectra\tt.csv"
#ratios = {"DBE": (1,10), "O": (0.1,20), "H": (0.1, 40)}
#df_output = FormulaRefiner(spectrum_path, -1, ratios)
