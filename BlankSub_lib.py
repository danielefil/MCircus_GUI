from pathlib import Path
import pandas as pd

def BlankSub(ResultPath, BlankRatio):
    FileList = []
    for _file in Path(ResultPath).glob('*.csv'):
        FileList.append(_file)
    
    blank_df = pd.read_csv(FileList[-1])
    blank_df['type'] = 'B'
    test_df = pd.read_csv(FileList[0])
    test_df['type'] = 'S'
    
    #df = pd.merge(blank_df, test_df)
    df = pd.concat([blank_df, test_df])
    a = df.groupby('Fromula Bruta').filter(lambda x: x.shape[0] >1)
    a.sort_values(by='Fromula Bruta')
    print(a.sort_values(by=['Fromula Bruta', 'type'], ascending = False))
    #for key, item in a:
    #    print(a.get_group(key))
    
    #####################################
    ########## FOR DEBUG ################

ResultPath = r'C:\Users\df426\Desktop\!!!!Filtri Ivan\Results'
BlankRatio = 10

BlankSub(ResultPath, BlankRatio)