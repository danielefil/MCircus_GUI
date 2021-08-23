import rawlib
from PyQt5 import QtCore, QtGui, QtWidgets, uic
from PyQt5.QtWidgets import QDialog, QMainWindow, QApplication, QFileDialog
from pathlib import Path
import sys

## USER DEFINED LIBRARIES ##

# Molecule class (for MM calculation) 
import molecule
import element
# Other functions
from Search_to_function_isopattern_10 import search_peak


class RawFilterDialog(QDialog):
    def __init__(self, lista, parent = None):   
        super(RawFilterDialog, self).__init__(parent) # Call the inherited classes __init__ method
        uic.loadUi('RawFilter.ui', self) # Load the .ui file
        self.setWindowTitle("Filter Selector")
        #CONNECTION
        self.SP_CBox.currentIndexChanged.connect(self.SelectionChange)
        self.SetFilter_btn.clicked.connect(self.SetFilter)
        
        self.passlista = lista
        _filenames = [i.stem for i in lista]
        
        #_filenames = [i.stem for i in self.passlista]
        self.SP_CBox.addItems(_filenames)

    
    def SelectionChange(self):
        selectedSpectraIndex = self.SP_CBox.currentIndex()
        Filterlist = rawlib.getScanFilter(str(self.passlista[selectedSpectraIndex]))
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
        
        #CONNECTION
        



class Ui(QtWidgets.QMainWindow):
    def __init__(self):   
        super(Ui, self).__init__() # Call the inherited classes __init__ method
        uic.loadUi('MassCircus_GUI_6.ui', self) # Load the .ui file
        
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
        
        #self.adducts = []
        #self.carica = 0

        #self.ppm_tolletance = self.ppm_spinbox.value()
        #self.da_tolletance = self.dalton_spinbox.value()
    
    # DISABLE ELEMENTS
    def grey_components(self):
        self.tabWidget.setTabEnabled(1, False)
        self.tabWidget.setTabEnabled(2, False)
        self.tabWidget.setTabEnabled(3, False)

        self.gBox_NoiseFilter.setEnabled(False)

        self.gBox_DB.setEnabled(False)

        #self.gBPositive.setEnabled(False)
        #self.gBNegative.setEnabled(False)
        #self.create_button.setEnabled(False)
        #self.find_button.setEnabled(False)
        #self.ppm_spinbox.setEnabled(False)
        #self.dalton_spinbox.setEnabled(False)
    

    # CONNECTIONS
    def enable_connection(self):
        #TAB 1 - INPUT
        self.OpenSP_btn.clicked.connect(self.openSpectraDialog)
        self.csv_rdbtn.toggled.connect(self.fileextension)
        self.raw_rdbtn.toggled.connect(self.fileextension)
        self.mzML_rdbtn.toggled.connect(self.fileextension)
        self.Next1_btn.clicked.connect(self.nextTab1_2)
        
        #TAB 2 - NOISE FILTER
        self.EnableFilter_cbtn.toggled.connect(self.Enable_Filtering)
        self.Next2_btn.clicked.connect(self.nextTab2_3)
        self.Next2_btn.clicked.connect(self.GetFilterParams)
        
        #TAB 3 - FIND METHOD
        self.EC_radio.toggled.connect(self.Enable_SearchMtd_Selector)
        self.DB_radio.toggled.connect(self.Enable_SearchMtd_Selector)
        self.EC_Open_btn.clicked.connect(self.openDataBaseDialog)
        self.DB_Open_btn.clicked.connect(self.openDataBaseDialog)
        self.Next3_btn.clicked.connect(self.nextTab3_4)
        #self.Next3_btn.clicked.connect(self.GetSearchMtd)

        #TAB 4 - SEARCH OPTIONS      
        #self.Positive_radio.toggled.connect(self.Enable_Adducts_Selector)
        #self.Negative_radio.toggled.connect(self.Enable_Adducts_Selector)
        #self.ppm_radio.toggled.connect(self.Enable_Finder_Selector)
        #self.dalton_radio.toggled.connect(self.Enable_Finder_Selector)
        #self.create_button.clicked.connect(self.charge_selector)
        #self.openDB_button.clicked.connect(self.openDatabaseDialog)
        #self.find_button.clicked.connect(self.finder)
    
    
    def nextTab1_2(self):
        if self.SpectraPath == '':    
            QtWidgets.QMessageBox.warning(self, "Warning", "Select spectra folder to continue")
        else:    
            currentTab = self.tabWidget.currentIndex()
            self.tabWidget.setTabEnabled(currentTab+1, True)
            self.tabWidget.setCurrentIndex(currentTab+1) 
    
    def nextTab2_3(self):
        currentTab = self.tabWidget.currentIndex()
        self.tabWidget.setTabEnabled(currentTab+1, True)
        self.tabWidget.setCurrentIndex(currentTab+1) 

    def nextTab3_4(self):
        if self.FindMethod == []:
           QtWidgets.QMessageBox.warning(self, "Warning", "Please select Compounds List or Elemental Composition file")  
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
            self.SP_folderPath = QFileDialog.getExistingDirectory(self, options=options)
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

    
    # ENABLE/DISABLE SEARCH METHOD --> ELEMENTAL COMPOSITION/COMPOUNDS LIST
    def Enable_SearchMtd_Selector(self):
        if self.EC_radio.isChecked():
            self.gBox_EC.setEnabled(True)
            self.gBox_DB.setEnabled(False)
            self.DB_line.clear()
        else:
            self.gBox_EC.setEnabled(False)
            self.gBox_DB.setEnabled(True)
            self.EC_line.clear()
    
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

    # OPEN ELEMENTAL COMPOSITION/COMPOUNDS LIST DIALOG
    def openDataBaseDialog(self):
        options = QFileDialog.Options()
        options |= QFileDialog.DontUseNativeDialog
        if self.EC_radio.isChecked():
            files, _ = QFileDialog.getOpenFileNames(self, "Select Elemental Composition file", "", "CSV Files (*.csv);;Text Files (*.txt)", options=options)
            if files:
                self.EC_line.setText(files[0])
                self.FindMethod = ['EC', files[0]]
        else:
            files, _ = QFileDialog.getOpenFileNames(self, "Select Compounds List file", "", "CSV Files (*.csv);;Text Files (*.txt)", options=options)    
            if files:
                self.DB_line.setText(files[0])
                self.FindMethod = ['DB', files[0]]
        print(self.test)

    
    




def main():
    # a new app instance
    app = QtWidgets.QApplication(sys.argv)
    window = Ui()
    window.setWindowTitle("MASS_CIRCUS - v3.0")
    # without this, the script exits immediately.
    sys.exit(app.exec_())


if __name__ == "__main__":
    main()
