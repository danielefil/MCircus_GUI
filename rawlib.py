
import pythoncom
pythoncom.CoInitialize()
import clr
#from System import *

clr.AddReference('System.Collections')
clr.AddReference('RawReader_dll/ThermoFisher.CommonCore.Data')
clr.AddReference('RawReader_dll/ThermoFisher.CommonCore.RawFileReader')
clr.AddReference('RawReader_dll/ThermoFisher.CommonCore.BackgroundSubtraction')
clr.AddReference('RawReader_dll/ThermoFisher.CommonCore.MassPrecisionEstimator')

from ThermoFisher.CommonCore.Data import ToleranceUnits
from ThermoFisher.CommonCore.Data import Extensions
from ThermoFisher.CommonCore.Data.Business import Device
from ThermoFisher.CommonCore.Data.Interfaces import IScanFilter
from ThermoFisher.CommonCore.RawFileReader import RawFileReaderAdapter



# function
def getScanFilter(rawfile):

    #from System.Collections import *
    # Create the IRawDataPlus object for accessing the RAW file
    _rawFile = RawFileReaderAdapter.FileFactory(rawfile)
    _rawFile.SelectInstrument(Device.MS, 1)
    
    # Get the first and last scan from the RAW file
    firstScanNumber = _rawFile.RunHeaderEx.FirstSpectrum
    lastScanNumber = _rawFile.RunHeaderEx.LastSpectrum

    FilterList = []
    for i in range(firstScanNumber, lastScanNumber+1):
        Filter = IScanFilter(_rawFile.GetFilterForScanNumber(i)).ToString()
        if Filter not in FilterList:
            FilterList.append(Filter)
        
    _rawFile.Dispose()    
    return(FilterList)


###################
#### FOR DEBUG ####
###################


#print(getScanFilter(r'C:/Users/df426/Desktop/RawReader_Py/GSH_NEM_Full_Scan_60K_FTMS.raw'))