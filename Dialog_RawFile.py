import RawReader_lib
from PyQt5 import uic
from PyQt5.QtWidgets import QDialog

class Ui(QDialog):
    def __init__(self, FileList, parent = None):   
        super(Ui, self).__init__(parent) # Call the inherited classes __init__ method
        uic.loadUi("RawFilter.ui", self) # Load the .ui file
        self.setWindowTitle("Filter Selector")
        #CONNECTION
        self.SP_CBox.currentIndexChanged.connect(self.SelectionChange)
        self.SetFilter_btn.clicked.connect(self.SetFilter)
        
        self.FileList = FileList
        _filenames = [i.stem for i in FileList]
        
        self.SP_CBox.addItems(_filenames)

    
    def SelectionChange(self):
        selectedSpectraIndex = self.SP_CBox.currentIndex()
        Filterlist = RawReader_lib.getScanFilter(str(self.FileList[selectedSpectraIndex]))
        self.Filter_CBox.clear()
        self.Filter_CBox.addItems(Filterlist)

    def RawConverter(self):
        for _file in self.FileList:
            print(_file, self.selectedFilter)
            RawReader_lib.GetAverage(str(_file), self.selectedFilter)  # AVG the spectra and Convert it to csv file
            
    
    def SetFilter(self):
        self.selectedFilter = self.Filter_CBox.currentText()
        self.RawConverter()
        self.close()

    