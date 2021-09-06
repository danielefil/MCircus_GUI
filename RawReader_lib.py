import platform
if platform.system() == 'Windows':
    import pythoncom
    pythoncom.CoInitialize()

import clr

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



def GetAverage(rawFile, scanFilter):
    '''Gets the average spectrum from the RAW file.

    Args:
        rawFile (IRawDataPlus): the RAW file being read.
        firstScanNumber (int): the first scan to consider for the averaged spectrum.
        lastScanNumber (int): the last scan to consider for the averaged spectrum.
        outputData (bool): the output data flag.
    '''
    _rawFile = RawFileReaderAdapter.FileFactory(rawFile)
    _rawFile.SelectInstrument(Device.MS, 1)
    
    # Get the first and last scan from the RAW file
    firstScanNumber = _rawFile.RunHeaderEx.FirstSpectrum
    lastScanNumber = _rawFile.RunHeaderEx.LastSpectrum
    # Create the mass options object that will be used when averaging
    # the scans
    
    options = Extensions.DefaultMassOptions(_rawFile)
    options.ToleranceUnits = ToleranceUnits.ppm
    options.Tolerance = 5.0

    # Get the scan filter for the first scan.  This scan filter will be used to located
    # scans within the given scan range of the same type
    #scanFilter = IScanFilter(rawFile.GetFilterForScanNumber(firstScanNumber))

    # Get the average mass spectrum for the provided scan range. In addition to getting the
    # average scan using a scan range, the library also provides a similar method that takes
    # a time range.
    averageScan = Extensions.AverageScansInScanRange(
        _rawFile, firstScanNumber, lastScanNumber, scanFilter, options)

    if averageScan.HasCentroidStream:
        print('Average spectrum ({} points)'.format(averageScan.CentroidScan.Length))

        # Print the spectral data (mass, intensity values)
        for i in range(averageScan.CentroidScan.Length):
            print('  {:.4f} {:.0f}'.format(averageScan.CentroidScan.Masses[i], averageScan.CentroidScan.Intensities[i]))


# Get a average spectrum from the RAW file for the first 15 scans in the file.



###################
#### FOR DEBUG ####
###################

#print(getScanFilter(r'C:/Users/df426/Desktop/RawReader_Py/GSH_NEM_Full_Scan_60K_FTMS.raw'))
#GetAverage(r'C:/Users/df426/Desktop/RawReader_Py/GSH_NEM_Full_Scan_60K_FTMS.raw', 1, 15, False)
