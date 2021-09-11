#import RawReader_lib
from PyQt5 import QtWidgets, uic
from PyQt5.QtWidgets import QFileDialog
from pathlib import Path
import sys

## USER DEFINED LIBRARIES ##


# Other functions
#from PatternSearch_lib import PatternSearch
import Dialog_mzMLFile
import Dialog_RawFile
import Dialog_FormulaFinder
import Dialog_DBFinder


class Ui(QtWidgets.QMainWindow):
    def __init__(self):   
        super(Ui, self).__init__() # Call the inherited classes __init__ method
        uic.loadUi("Ui/MassCircus_GUI_7.ui", self) # Load the .ui file
        
        # INIT FUNCTIONS
        self.show() # Show the GUI
        self.grey_components()
        self.enable_connection()
        
        # GLOBAL VARIABLES
        self.Spectralist = []
        self.fileext = None
        self.SpectraPath = ""
        self.BlankFilePath = False
        self.Noise_BlankParams = [False, 0, 0, False, 10]
        self.FindMethod = []
        

    
    # DISABLED ELEMENTS
    def grey_components(self):
        self.tabWidget.setTabEnabled(1, False)
        self.tabWidget.setTabEnabled(2, False)
        self.tabWidget.setTabEnabled(3, False)
        self.gBox_NoiseFilter.setEnabled(False)
        self.gBox_BlankSubtract.setEnabled(False)


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

        #TAB  - BLANK SUBSTRACTION
        self.EnableBlank_cbtn.toggled.connect(self.Enable_Blank)
        self.Next3_btn.clicked.connect(self.nextTab2)
        self.OpenBL_btn.clicked.connect(self.GetBlankFile)
        
        #TAB 4 - FIND METHOD
        self.DB_Dialog_btn.clicked.connect(self.DB_OpenDialog)
        self.EC_Dialog_btn.clicked.connect(self.EC_OpenDialog)

    
    def nextTab(self):
        if self.SpectraPath == "":    
            QtWidgets.QMessageBox.warning(self, "Warning", "Select spectra folder to continue")
        else:    
            currentTab = self.tabWidget.currentIndex()
            self.tabWidget.setTabEnabled(currentTab+1, True)
            self.tabWidget.setCurrentIndex(currentTab+1) 
    
    def nextTab2(self):
        if (self.EnableBlank_cbtn.isChecked() and self.BlankFilePath == False):
            QtWidgets.QMessageBox.warning(self, "Warning", "Select spectra folder to continue or disable Blank subtractions")
        elif (self.EnableBlank_cbtn.isChecked() and self.BlankFilePath == True):
            currentTab = self.tabWidget.currentIndex()
            self.tabWidget.setTabEnabled(currentTab+1, True)
            self.tabWidget.setCurrentIndex(currentTab+1)
        else:    
            currentTab = self.tabWidget.currentIndex()
            self.tabWidget.setTabEnabled(currentTab+1, True)
            self.tabWidget.setCurrentIndex(currentTab+1) 

    # FILES TYPE SELECTOR 
    def fileextension(self):
        if self.csv_rdbtn.isChecked() == True:
            self.fileext = "*.csv"
        if self.raw_rdbtn.isChecked() == True:
            self.fileext = "*.raw"
        if self.mzML_rdbtn.isChecked() == True:
            self.fileext = "*.mzML"

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
                if self.fileext == "*.raw":
                    # Apro finestra per selezione dei filtri
                    RAW_Dialog = Dialog_RawFile.Ui(self.Spectralist)
                    RAW_Dialog.exec()
                elif self.fileext == "*.mzML":
                    mzML_Dialog = Dialog_mzMLFile.Ui(self.Spectralist)
                    mzML_Dialog.exec()
    #### Devo ritornare self.spectralist con i dati *.csv 
                    self.Spectralist = mzML_Dialog.SetFilter()
    
    
    # ENABLE/DISABLE NOISE FILTERING
    def Enable_Filtering(self):
        if self.EnableFilter_cbtn.isChecked():
            self.gBox_NoiseFilter.setEnabled(True)
        else:
            self.gBox_NoiseFilter.setEnabled(False)

    # ENABLE/DISABLE BLANK SUBTRACTION
    def Enable_Blank(self):
        if self.EnableBlank_cbtn.isChecked():
            self.gBox_BlankSubtract.setEnabled(True)
            self.Noise_BlankParams[3] = True
        else:
            self.gBox_BlankSubtract.setEnabled(False)
            self.Noise_BlankParams[3] = False
    
    # GET NOISE FILTER PARAMETERS
    def GetFilterParams(self):
        if self.EnableFilter_cbtn.isChecked():
            self.Noise_BlankParams = [True, self.IntensePerc_spinbox.value(), self.BreakCount_spinbox.value(), False, 10]


    def GetBlankFile(self):
        options = QFileDialog.Options()
        options |= QFileDialog.DontUseNativeDialog
        files, _ = QFileDialog.getOpenFileNames(
            self, "Select Blank Spectra", "", "Text Files (*.txt);;csv Files (*.csv)", options=options)
        if files:
            self.BL_line.setText(files[0])
            self.BlankFilePath = True
            #self.Spectralist.insert(0, files[0]) ##metto il bianco all fine della mia lista dei campioni
            self.Spectralist.append(files[0])

    #OPEN COMPOUNDS LIST SEARCH MODE
    def DB_OpenDialog(self):
        DB_Dialog = Dialog_DBFinder.Ui(self.Spectralist, self.Noise_BlankParams)
        DB_Dialog.exec()
    
    #OPEN ELEMENTAL COMPOSITION SEARCH MODE
    def EC_OpenDialog(self):
        EC_Dialog = Dialog_FormulaFinder.Ui(self.Spectralist, self.Noise_BlankParams)
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
