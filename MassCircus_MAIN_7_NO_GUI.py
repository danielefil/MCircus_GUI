from pathlib import Path
import sys

## USER DEFINED LIBRARIES ##
# GUI layout
# Molecule class (for MM calculation) 
import molecule
import element
# Other functions
from PatternSearch_lib import PatternSearch
import time


# Cartella contenente gli spettri
SP_folderPath = r"C:\Users\df426\Desktop\TEST_MassCircus_GUI"
#SP_folderPath = r"C:\Users\df426\Desktop\AnalisiCromo\Spectra"
files = Path(SP_folderPath)

#addotti = ["Cl", "Hp"] #Lista degli addotti Hp --> per perdita H+
addotti = ["El"] #Lista degli addotti El --> perdita elettrone
carica = -3 #Numero di cariche
# Percorso che contiene il database dei composti da cercare
DB_path = r"C:\Users\df426\Desktop\TEST_MassCircus_GUI\DB\Leganti_CN- neg.dat"
#DB_path = r"C:\Users\df426\Desktop\AnalisiCromo\Formule\Part2_2020_7_3_cromoacetato_gallico_1a3_h2o_meoh_1a100_400-2000_NEG.dat"
search_property = ["ppm", 10] #Modalita" di ricerca: ppm/dalton, tolleranza 
# Lista etichetta degli addotti: +H(+), -H(+)
#addotti_label = ["+Cl(-)","-H(+)"]
addotti_label = ["-"]
filterValues = [False, 0, 0]


FilesList = []

for CurrentFile in files.glob("*.csv"):
    FilesList.append(CurrentFile)

start_time = time.time()
PatternSearch(FilesList, DB_path, addotti, carica,  search_property, addotti_label, Filtering=filterValues)
print(round(time.time() - start_time, 2), "seconds")

