from pathlib import Path
import numpy as np
import pandas as pd

def BlankSub(ResultsPath, BlankRatio):
    FileList = []
    for _file in Path(ResultsPath).glob("*.csv"):
        FileList.append(_file)
    
    df_Blank = pd.read_csv(FileList[-1])
    
    for _elem in FileList[:-1]:
        
        df_Sample = pd.read_csv(_elem)
        df_Sample["Ratio"] = np.NaN
        BlankFormulas = df_Blank["m/z(teorico)"].tolist()
        for index, row in df_Sample.iterrows():
            if row["m/z(teorico)"] in BlankFormulas:
                blankindex = BlankFormulas.index(row["m/z(teorico)"])
                df_Sample.at[index, "Ratio"] = (df_Sample.iloc[index]["Abs. Int."])/(df_Blank.iloc[blankindex]["Abs. Int."])
        df_output = df_Sample[(df_Sample["Ratio"].isna()) | (df_Sample["Ratio"] > BlankRatio)]
        del(df_output["Ratio"])
        
        newpath = (str(_elem)).replace('RESULTS_', 'RESULTS_BLK_')
        Path.unlink(_elem)
        df_output.to_csv(newpath, index= None)

#####################################
########## FOR DEBUG ################

ResultPath = r"C:\Users\df426\Desktop\!!!!Filtri Ivan\Results"
BlankRatio = 10
BlankSub(ResultPath, BlankRatio)
