import RawReader_lib
from PyQt5 import QtCore, QtGui, QtWidgets, uic
from PyQt5.QtWidgets import QDialog, QMainWindow, QApplication, QFileDialog
from pathlib import Path
import sys
import csv

## USER DEFINED LIBRARIES ##

# Molecule class (for MM calculation) 
import molecule
import element
# Other functions
from Search_to_function_isopattern_10 import search_peak
import Dialog_FormulaFinder
import Dialog_DBFinder


class RawFilterDialog(QDialog):
    def __init__(self, FileList, parent = None):   
        super(RawFilterDialog, self).__init__(parent) # Call the inherited classes __init__ method
        uic.loadUi('RawFilter.ui', self) # Load the .ui file
        self.setWindowTitle("Filter Selector")
        #CONNECTION
        self.SP_CBox.currentIndexChanged.connect(self.SelectionChange)
        self.SetFilter_btn.clicked.connect(self.SetFilter)
        
        self.passlista = FileList
        _filenames = [i.stem for i in FileList]
        
        #_filenames = [i.stem for i in self.passlista]
        self.SP_CBox.addItems(_filenames)

    
    def SelectionChange(self):
        selectedSpectraIndex = self.SP_CBox.currentIndex()
        Filterlist = RawReader_lib.getScanFilter(str(self.passlista[selectedSpectraIndex]))
        self.Filter_CBox.clear()
        self.Filter_CBox.addItems(Filterlist)


    def SetFilter(self):
        self.selectedFilter = self.Filter_CBox.currentText()
        print(self.selectedFilter)
        self.close()

class IsoPatternOptions(QDialog):
    def __init__(self, parent=None):
        # Call the inherited classes __init__ method
        super(IsoPatternOptions, self).__init__(parent)
        uic.loadUi('IsoPatternOptions.ui', self)  # Load the .ui file
        self.setWindowTitle("Isotopic Pattern Calculator Options")
        

class Ui(QtWidgets.QMainWindow):
    def __init__(self):   
        super(Ui, self).__init__() # Call the inherited classes __init__ method
        uic.loadUi('MassCircus_GUI_7.ui', self) # Load the .ui file
        
        # INIT FUNCTIONS
        self.show() # Show the GUI
        self.grey_components()
        self.enable_connection()
        
        # GLOBAL VARIABLES
        self.Spectralist = []
        self.fileext = None
        self.SpectraPath = ''
        self.NoiseFilterParams = [False, 0, 0]
        self.FindMethod = []
        

    
    # DISABLE ELEMENTS
    def grey_components(self):
        self.tabWidget.setTabEnabled(1, False)
        self.tabWidget.setTabEnabled(2, False)
        ###self.tabWidget.setTabEnabled(3, False)

        self.gBox_NoiseFilter.setEnabled(False)
    

    # CONNECTIONS
    def enable_connection(self):
        #TAB 1 - INPUT
        self.OpenSP_btn.clicked.connect(self.openSpectraDialog)
        self.csv_rdbtn.toggled.connect(self.fileextension)
        self.raw_rdbtn.toggled.connect(self.fileextension)
        self.mzML_rdbtn.toggled.connect(self.fileextension)
        self.Next1_btn.clicked.connect(self.nextTab)
        
        #TAB 2 - NOISE FILTER
        self.EnableFilter_cbtn.toggled.connect(self.Enable_Filtering)
        self.Next2_btn.clicked.connect(self.nextTab)
        self.Next2_btn.clicked.connect(self.GetFilterParams)
        
        #TAB 3 - FIND METHOD
        self.DB_Dialog_btn.clicked.connect(self.DB_OpenDialog)
        self.EC_Dialog_btn.clicked.connect(self.EC_OpenDialog)


    
    
    def nextTab(self):
        if self.SpectraPath == '':    
            QtWidgets.QMessageBox.warning(self, "Warning", "Select spectra folder to continue")
        else:    
            currentTab = self.tabWidget.currentIndex()
            self.tabWidget.setTabEnabled(currentTab+1, True)
            self.tabWidget.setCurrentIndex(currentTab+1) 
    

    # FILES TYPE SELECTOR 
    def fileextension(self):
        if self.csv_rdbtn.isChecked() == True:
            self.fileext = '*.csv'
        if self.raw_rdbtn.isChecked() == True:
            self.fileext = '*.raw'
        if self.mzML_rdbtn.isChecked() == True:
            self.fileext = '*.mzML'

    # OPEN FILES DIALOG - SPECTRA (MULTIPLE)
    def openSpectraDialog(self):
        if self.fileext == None:
            QtWidgets.QMessageBox.warning(self, "Warning", "Select input file type")
        else:
            options = QFileDialog.Options()
            options |= QFileDialog.DontUseNativeDialog
            self.SP_folderPath = QFileDialog.getExistingDirectory()
            if self.SP_folderPath:
                self.SP_line.setText(self.SP_folderPath)
                self.SpectraPath = Path(self.SP_folderPath)
        
                for _file in self.SpectraPath.glob(self.fileext):
                    self.Spectralist.append(_file)
                #print(self.Spectralist)   ## FOR DEBUG
                if self.fileext == '*.raw':
                    # Apro finestra per selezione dei filtri
                    dlg = RawFilterDialog(self.Spectralist)
                    dlg.exec()

    
    
    # ENABLE/DISABLE NOISE FILTERING
    def Enable_Filtering(self):
        if self.EnableFilter_cbtn.isChecked():
            self.gBox_NoiseFilter.setEnabled(True)
        else:
            self.gBox_NoiseFilter.setEnabled(False)
    
    # GET NOISE FILTER PARAMETERS
    def GetFilterParams(self):
        if self.EnableFilter_cbtn.isChecked():
            self.NoiseFilterParams = [True, self.IntensePerc_spinbox.value(), self.BreakCount_spinbox.value()]
        print(self.NoiseFilterParams)

    #OPEN COMPOUNDS LIST SEARCH MODE
    def DB_OpenDialog(self):
        DB_Dialog = Dialog_DBFinder.Ui(self.Spectralist)
        DB_Dialog.exec()
    
    #OPEN ELEMENTAL COMPOSITION SEARCH MODE
    def EC_OpenDialog(self):
        EC_Dialog = Dialog_FormulaFinder.Ui(self.Spectralist)
        EC_Dialog.exec()
    

def main():
    # a new app instance
    app = QtWidgets.QApplication(sys.argv)
    window = Ui()
    window.setWindowTitle("MASS_CIRCUS - v7.0")
    # without this, the script exits immediately.
    sys.exit(app.exec_())


if __name__ == "__main__":
    main()
