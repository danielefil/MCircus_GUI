import mzMLReader_lib
from pathlib import Path
from PyQt5 import uic
from PyQt5.QtWidgets import QDialog

class Ui(QDialog):
    def __init__(self, FileList, parent = None):   
        super(Ui, self).__init__(parent) # Call the inherited classes __init__ method
        uic.loadUi('FilterDialog.ui', self) # Load the .ui file
        self.setWindowTitle("Filter Selector")
        #CONNECTION
        self.SP_CBox.currentIndexChanged.connect(self.SelectionChange)
        self.SetFilter_btn.clicked.connect(self.SetFilter)
        
        self.FileList = FileList
        _filenames = [i.stem for i in FileList]
        
        self.SP_CBox.addItems(_filenames)

     
    def SelectionChange(self):
        selectedSpectraIndex = self.SP_CBox.currentIndex()
        Filterlist = mzMLReader_lib.getScanFilter(str(self.FileList[selectedSpectraIndex]))
        self.Filter_CBox.clear()
        self.Filter_CBox.addItems(Filterlist)
    
    
    def SetFilter(self):
        self.selectedFilter = self.Filter_CBox.currentText()
        self.NewFileList = []
        
        tmp_path = (Path(__file__).parent).joinpath('tmp') 
        try:
            tmp_path.mkdir(parents=True, exist_ok=True)
        except FileExistsError:
            pass

        for _file in self.FileList:
            AvgSpectraFilePath = mzMLReader_lib.getAverageSpectra(str(_file), self.selectedFilter, tmp_path)
            self.NewFileList.append(AvgSpectraFilePath)
    
        self.close()
        return(self.NewFileList)
