import rawlib
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


##################################################################################################################
################################ DB_DialogFinder


class DB_DialogFinder(QDialog):
    def __init__(self, lista, parent = None):   
        super(DB_DialogFinder, self).__init__(parent) # Call the inherited classes __init__ method
        uic.loadUi('Dialog_ListFinder.ui', self) # Load the .ui file
        self.setWindowTitle("Compound List Finder")

        
        #DISABLED
        self.gBPositive.setEnabled(False)
        self.gBNegative.setEnabled(False)
        self.ppm_spinbox.setEnabled(False)
        self.dalton_spinbox.setEnabled(False)
        self.find_button.setEnabled(False)
        self.gBoxCharge.setEnabled(False)
        self.DB_Create_btn.setEnabled(False)

        #CONNECTION
        self.DB_Open_btn.clicked.connect(self.openDatabase_Dialog)
        self.Positive_radio.toggled.connect(self.Enable_Adducts_Selector)
        self.Negative_radio.toggled.connect(self.Enable_Adducts_Selector)
        self.ppm_radio.toggled.connect(self.Enable_Finder_Selector)
        self.dalton_radio.toggled.connect(self.Enable_Finder_Selector)
        #self.DB_Create_btn.clicked.connect(self.charge_selector)
        #self.find_button.clicked.connect(self.finder)
    
    def openDatabase_Dialog(self):
        options = QFileDialog.Options()
        options |= QFileDialog.DontUseNativeDialog
        files, _ = QFileDialog.getOpenFileNames(self, "Select Compounds List file", "", "CSV Files (*.csv);;Text Files (*.txt)", options=options)
        if files:
            self.DB_line.setText(files[0])
            self.DB_path = files[0]
        print(self.DB_path)
    
    # ENABLE/DISABLE +/- ADDUCTOR SELECTOR
    def Enable_Adducts_Selector(self):
        if self.Positive_radio.isChecked():
            self.gBPositive.setEnabled(True)
            self.gBNegative.setEnabled(False)
            self.DB_Create_btn.setEnabled(True)
            self.gBoxCharge.setEnabled(True)
        else:
            self.gBPositive.setEnabled(False)
            self.gBNegative.setEnabled(True)
            self.DB_Create_btn.setEnabled(True)
            self.gBoxCharge.setEnabled(True)

    # ENABLE/DISABLE PPM/DALTON SEARCH MODE
    def Enable_Finder_Selector(self):
        if self.ppm_radio.isChecked():
            self.ppm_spinbox.setEnabled(True)
            self.dalton_spinbox.setEnabled(False)
            self.find_button.setEnabled(True)
            self.search_mode = "ppm"
        else:
            self.ppm_spinbox.setEnabled(False)
            self.dalton_spinbox.setEnabled(True)
            self.find_button.setEnabled(True)
            self.search_mode = "dalton"

################################ DB_DialogFinder
##################################################################################################################

class EC_DialogFinder(QDialog):
    def __init__(self, lista, parent = None):   
        super(EC_DialogFinder, self).__init__(parent) # Call the inherited classes __init__ method
        uic.loadUi('Dialog_ElementFinder.ui', self) # Load the .ui file
        self.setWindowTitle("Elemental Composition Finder")

        self.EC_Open_btn.clicked.connect(self.openElementalComp_Dialog)

        # OPEN FILES DIALOG - DATABASE
    def openElementalComp_Dialog(self):
        options = QFileDialog.Options()
        options |= QFileDialog.DontUseNativeDialog
        files, _ = QFileDialog.getOpenFileNames(self, "Select Elemental Composition file", "", "CSV Files (*.csv);;Text Files (*.txt)", options=options)
        if files:
            self.EC_line.setText(files[0])
            self.EC_path = files[0]
            #print(self.EC_path)
            with open(self.EC_path) as f:
                reader = csv.reader(f)
                mylist = list(reader)
            rowPosition = self.tableWidget.rowCount()
            self.tableWidget.insertRow(rowPosition)    
            self.tableWidget.setItem(rowPosition, 0, QtGui.QTextTable('CIAO'))


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
        DB_Dialog = DB_DialogFinder(self.Spectralist)
        DB_Dialog.exec()
    
    #OPEN ELEMENTAL COMPOSITION SEARCH MODE
    def EC_OpenDialog(self):
        EC_Dialog = EC_DialogFinder(self.Spectralist)
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
