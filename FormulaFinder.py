import time
from element import Element
import re
import pandas as pd
import numpy as np
from progressbar import ProgressBar, ETA, FileTransferSpeed, Bar, Percentage


### ATOM CLASS ###
# TO BE IMPLEMENTED IN A DIFFERENT WAY... 
class Atom:
    def __init__(self, Simbol, Label, Mass, Min, Max):
        self.Simbol = Simbol
        self.Label = Label
        self.Mass = Mass
        self.Max = Max
        self.Min = Min


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
    ratios = int(l.get(atom, 0))/int(l.get('C', 0))
    return ratios

def carbon(formula):
    l = dict(re.findall("(\D+)(\d+)", formula))
    _carbon = l.get('C', 0)
    return (_carbon)

### CLEANER - Rimuove gli atomi con pedice 0 -
def cleaner(formula):
    parsed = re.findall(r"([A-Z][a-z]*)(\d*)|(\()|(\))(\d*)", formula)
    cleand_formula = ''
    for element_details in parsed:
        element = element_details[0]
        element_count = element_details[1]
        if element_count != '0':
            cleand_formula = cleand_formula + element + element_count
    if cleand_formula != '':
        return cleand_formula
    else:
        return None

### DECOMPOSER ###
def decomposer(Mtot, atoms, limits, mass=0, formula='', output=[]):
    if atoms != []:
        if Mtot >= atoms[0].Mass:
            Nmax = int(min(atoms[0].Max, (Mtot)//atoms[0].Mass))
            Nmin = atoms[0].Min
            if len(atoms) == 1: # Se ultimo atomo correggo Nmin
                Nmin = int(max(atoms[0].Min, (Mtot)//atoms[0].Mass))
            for A in list(range(Nmin, Nmax+1)):
                NewMtot = Mtot - A*atoms[0].Mass
                Newmass = mass + A*atoms[0].Mass
                NewFormula = formula + str(atoms[0].Simbol)+str(A)
                NewAtom = atoms[1:]
                if limits[0] < Newmass < limits[1]:
                    output.append((str(NewFormula), round(Newmass,5)))
                decomposer(NewMtot, NewAtom, limits, Newmass, NewFormula, output)

        else:
            atoms = atoms[1:]
            decomposer(Mtot, atoms, limits, mass, formula, output)
    
    return output    

# # FILTER -- TO BE IMPLEMENTED


def Calc_filter(df_results, charge: int, filtri: dict):

    ## pulisco le formule
    df_results['Formula'] = df_results['Formula'].apply(cleaner)

    ## pulisco le formule senza carbonio
    df_results = df_results.drop(
        df_results[df_results['Formula'].apply(carbon) == 0].index)

    ## calcolo la differenza in ppm
    #FRO M+ and M-
    adduct_corr = charge*0.00054387
    df_results['ppm'] = df_results.apply(lambda x: ppm_calc(x['m/z'], (x['Neutral Mass']-adduct_corr)), axis=1)
    #FOR PROTONATION ADN DEPROTONATION
    #adduct_corr = charge*1.0072764
    #df_results['ppm'] = df_results.apply(lambda x: ppm_calc(x['m/z'], (x['Neutral Mass']+adduct_corr)), axis=1)

    for key, values in filtri.items():
        if key == 'DBE':
            ## calcolo DBE
            df_results[key] = df_results['Formula'].apply(DBE)
            df_results = df_results[(df_results[key] >= values[0]) & (
                df_results[key] <= values[1])]
        else:
            df_results[key + '/C'] = df_results.apply(
                lambda x: ratio_calc(x['Formula'], key), axis=1)
            df_results = df_results[(
                df_results[key + '/C'] >= values[0]) & (df_results[key + '/C'] <= values[1])]
            #print(key, values[0], values[1])

    df_results = df_results.reset_index(drop=False)
    return df_results


######################################
###########  MAIN PROGRAM  ###########
######################################


#S = Atom('S', 'Sulfur', 31.97207069, 0, 2)
#N = Atom('N', 'Nitrogen', 14.0030740052, 0, 5)
Cr = Atom('Cr', 'Crome', 51.9405119, 1, 3)
O = Atom('O', 'Oxygen', 15.9949146221, 1, 50)
C = Atom('C', 'Carbon', 12.0, 1, 50)
H = Atom('H', 'Hydrogen', 1.0078250321, 1, 50)


## WIN PATH
spectrum_path = r'C:\Users\df426\Desktop\AnalisiCromo\Spectra\Part2_2020_7_3_cromoacetato_gallico_1a3_h2o_meoh_1a100_400-2000_NEG.csv'
## MAC PATH
#spectrum_path = '/Users/danielefilippi/Desktop/negF1S1_100-650_cleaned.csv'

df_sp = pd.read_csv(spectrum_path, dtype={'Mass [m/z]': float, 'Intensity': float})
#spectra = np.round(df_sp.to_numpy(), 5)
spectra = df_sp.to_numpy()


atoms = [Cr, O, C, H]
ppm = 10
out = []
charge = -1 ##oppure -1

widgets = [' <<<', Bar(),'>>> ', Percentage(), ' ', ETA()]
pbar = ProgressBar(widgets=widgets)

#for values in spectra:
for values in pbar(spectra):
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
    
df_output = pd.DataFrame(out, columns=['m/z', 'Intensity' , 'Formula', 'Neutral Mass'])

# lista contenete gli atomi sui quali voglio calcolare i rapporti con il carbonio
ratios = {'DBE': (1,25), 'O': (0.4,3), 'H': (0.5, 3), 'S': (0, 0.2)}
df_output = Calc_filter(df_output, charge, ratios)

df_output.to_csv(
    r'C:\Users\df426\Desktop\Part2_2020_7_3_cromoacetato_gallico_1a3_h2o_meoh_1a100_400-2000_NEG.csv')




