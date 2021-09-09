from scipy import optimize
from pathlib import Path
import pandas as pd
import numpy as np
import pymzml


def meanMzInsts(mzlist: list, ilist: list, runs: int, dmz: float):
    spectra = np.column_stack((mzlist, ilist))
    spectra = spectra[np.argsort(spectra[:, 0])]

    mzdiff = np.diff(spectra[:, 0])
    group = np.arange(0, 1)
    group = np.append(group, (mzdiff >= dmz).astype(int))

    grupped = np.cumsum(group)
    grupped = grupped + 1

    # creo 2D array 1col = gruppo, 2col = mz, 3col = ints

    new_spectra = np.vstack((grupped, spectra[:, 0], spectra[:, 1])).T
    df = pd.DataFrame(new_spectra, columns=['key', 'mz', 'ints'])

    mean_mz = df.groupby('key').mz.mean()
    mean_ints = df.groupby('key').ints.agg(lambda x: (x.sum() / runs))
   
    averaged_spectra = (mean_mz.to_frame().join(mean_ints)) 
    return(averaged_spectra)


def GenTmpFolder():
    tmp_path = (Path(__file__).parent).joinpath('tmp')
    try:
        tmp_path.mkdir(parents=True, exist_ok=True)
    except FileExistsError:
        pass


def getScanFilter(mzml_file_path:str):
    mzmlFile = pymzml.run.Reader(mzml_file_path)
    filtri = set([])
    for spectra in mzmlFile:
        filtri.add(str(spectra['MS:1000512']))
    
    filtri = list(filtri)
    filtri.sort()
    return(filtri)

def getAverageSpectra(mzMLFilePath, selected_filter:str, tmp_path):
    print(mzMLFilePath)
    mzmlFile = pymzml.run.Reader(mzMLFilePath)
    mzlist = []
    ilist = []
    for i, spectra in enumerate(mzmlFile, 1):
        if str(spectra['MS:1000512']) == str(selected_filter):
            mzlist.extend(spectra.mz.tolist())
            ilist.extend(spectra.i.tolist())
    #Leggo gli spettri che corrispondo al filtro selezionato e ne calcolo la media
    
    Filename = str(tmp_path)+ "/" + str(Path(mzMLFilePath).name)
    AvgSpectra = meanMzInsts(mzlist, ilist, i, 0.001)
    AvgSpectra.to_csv(Filename, index = False)
    print(Filename)
    return(Filename)
