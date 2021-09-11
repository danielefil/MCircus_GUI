from pathlib import Path
import numpy as np
import pandas as pd

def BlankSub(ResultsPath, BlankRatio):
    FileList = []
    for _file in Path(ResultsPath).glob("*.csv"):
        FileList.append(_file)
    
    df_Blank = pd.read_csv(FileList[-1])
    df_Sample = pd.read_csv(FileList[0])
    df_Sample["Ratio"] = np.NaN
    BlankFormulas = df_Blank["Formula"].tolist()

    for index, row in df_Sample.iterrows():
        if row["Formula"] in BlankFormulas:
            df_Sample.at[index, "Ratio"] = (df_Sample.iloc[index]["Abs. Int."])/(df_Blank.iloc[index]["Abs. Int."])
    
    df_output = df_Sample[(df_Sample["Ratio"].notna()) & (df_Sample["Ratio"] > BlankRatio)]
    del(df_output["Ratio"])
    
    
#####################################
########## FOR DEBUG ################

#ResultPath = r"C:\Users\df426\Desktop\!!!!Filtri Ivan\Results"
#BlankRatio = 0.5
#BlankSub(ResultPath, BlankRatio)
