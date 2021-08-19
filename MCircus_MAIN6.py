from PyQt5 import QtCore, QtGui, QtWidgets, uic
from PyQt5.QtWidgets import QMainWindow, QApplication, QFileDialog
from pathlib import Path
import sys

## USER DEFINED LIBRARIES ##
# GUI layout
#import MassCircus_GUI_6
# Molecule class (for MM calculation) 
import molecule
import element
# Other functions
from Search_to_function_isopattern_10 import search_peak


class Ui(QtWidgets.QMainWindow):
    def __init__(self):   
        super(Ui, self).__init__() # Call the inherited classes __init__ method
        uic.loadUi('MassCircus_GUI_6.ui', self) # Load the .ui file
        self.show() # Show the GUI
    
'''
class MainWindow(QtWidgets.QMainWindow, MassCircus_GUI_6.Ui_MainWindow):

    def __init__(self):

        # Setting and connecting all GUI Components
        super(MainWindow, self).__init__()
        self.ui = MassCircus_GUI_6.Ui_MainWindow()
        self.ui.setupUi(self)
        self.grey_components()
        self.enable_connection()
        self.addotti = []
        self.filterValues = [False, 0, 0]
        self.carica = 0
        self.DB_path = ""
        self.SP_path = ""
        self.ppm_tolletance = self.ui.ppm_spinbox.value()
        self.da_tolletance = self.ui.dalton_spinbox.value()
        self.search_mode = ""

        # DISABLE ELEMENTS
    def grey_components(self):
        self.ui.gBPositive.setEnabled(False)
        self.ui.gBNegative.setEnabled(False)
        self.ui.create_button.setEnabled(False)
        self.ui.find_button.setEnabled(False)
        self.ui.ppm_spinbox.setEnabled(False)
        self.ui.dalton_spinbox.setEnabled(False)
        self.ui.gBFilter.setEnabled(False)
    
        # CONNECTIONS
    def enable_connection(self):
        self.ui.Positive_radio.toggled.connect(self.Enable_Adducts_Selector)
        self.ui.Negative_radio.toggled.connect(self.Enable_Adducts_Selector)
        self.ui.ppm_radio.toggled.connect(self.Enable_Finder_Selector)
        self.ui.dalton_radio.toggled.connect(self.Enable_Finder_Selector)
        self.ui.cBFilter.toggled.connect(self.Enable_Filtering)

        self.ui.create_button.clicked.connect(self.charge_selector)
        self.ui.openDB_button.clicked.connect(self.openDatabaseDialog)
        self.ui.openSP_button.clicked.connect(self.openSpectraDialog)
        self.ui.find_button.clicked.connect(self.finder)

        # ENABLE/DISABLE +/- ADDUCTOR SELECTOR
    def Enable_Adducts_Selector(self):
        if self.ui.Positive_radio.isChecked():
            self.ui.gBPositive.setEnabled(True)
            self.ui.gBNegative.setEnabled(False)
            self.ui.create_button.setEnabled(True)
        else:
            self.ui.gBPositive.setEnabled(False)
            self.ui.gBNegative.setEnabled(True)
            self.ui.create_button.setEnabled(True)

    def Enable_Filtering(self):
        if self.ui.cBFilter.isChecked():
            self.ui.gBFilter.setEnabled(True)
            self.filterValues[0] = True
        else:
            self.ui.gBFilter.setEnabled(False)
            self.filterValues[0] = False

        # ENABLE/DISABLE PPM/DALTON SEARCH MODE
    def Enable_Finder_Selector(self):
        if self.ui.ppm_radio.isChecked():
            self.ui.ppm_spinbox.setEnabled(True)
            self.ui.dalton_spinbox.setEnabled(False)
            self.ui.find_button.setEnabled(True)
            self.search_mode = "ppm"
        else:
            self.ui.ppm_spinbox.setEnabled(False)
            self.ui.dalton_spinbox.setEnabled(True)
            self.ui.find_button.setEnabled(True)
            self.search_mode = "dalton"


    def charge_selector(self):
        if self.ui.Positive_radio.isChecked():
            self.positive_adducts_creator()
        else:
            self.negative_adducts_creator()

        # NEGATIVE ADDUCT LIST CREATOR
    def negative_adducts_creator(self):
        self.addotti = []
        self.addotti_label = []
        if self.ui.cBFormiato.isChecked():
            self.addotti.append("HCOO")
            self.addotti_label.append("+fo(-)")
        if self.ui.cBAcetato.isChecked():
            self.addotti.append("C2H3O2")
            self.addotti_label.append("+ac(-)")
        if self.ui.cBCloro.isChecked():
            self.addotti.append("Cl")
            self.addotti_label.append("+Cl(-)")
        if self.ui.cBProtone_neg.isChecked():
            self.addotti.append("Hp")
            self.addotti_label.append("-H(+)")
        self.carica = -int(self.ui.charge_number_comboBox.currentText())
        # MESSAGGIO OPERAZIONE COMPLETATA
        QtWidgets.QMessageBox.about(self, "Message", "Adducts list Created")

        # POSITIVE ADDUCT LIST CREATOR
    def positive_adducts_creator(self):
        self.addotti = []
        self.addotti_label = []
        if self.ui.cBPotassio.isChecked():
            self.addotti.append("K")
            self.addotti_label.append("+K(+)")
        if self.ui.cBSodio.isChecked():
            self.addotti.append("Na")
            self.addotti_label.append("+Na(+)")
        if self.ui.cBAmmonio.isChecked():
            self.addotti.append("NH4")
            self.addotti_label.append("+am(+)")
        if self.ui.cBProtone.isChecked():
            self.addotti.append("H")
            self.addotti_label.append("+H(+)")
        self.carica = int(self.ui.charge_number_comboBox.currentText())
        # MESSAGGIO OPERAZIONE COMPLETATA
        QtWidgets.QMessageBox.about(self, "Message", "Adducts list Created")
    
        # OPEN FILES DIALOG - DATABASE
    def openDatabaseDialog(self):
        options = QFileDialog.Options()
        options |= QFileDialog.DontUseNativeDialog
        files, _ = QFileDialog.getOpenFileNames(self, "Select database file", "", "All Files (*);;Text Files (*.txt)", options=options)
        if files:
            self.ui.DB_line.setText(files[0])
            self.DB_path = files[0]

        # OPEN FILES DIALOG - SPECTRA (MULTIPLE)
    def openSpectraDialog(self):
        options = QFileDialog.Options()
        options |= QFileDialog.DontUseNativeDialog
        self.SP_folderPath = QFileDialog.getExistingDirectory()
        if self.SP_folderPath:
            self.ui.SP_line.setText(self.SP_folderPath)
            self.files = Path(self.SP_folderPath)

        # FINDER
    def finder(self):
        self.filterValues[1] = self.ui.IntensePerc_spinbox.value()
        self.filterValues[2] = self.ui.BreakCount_spinbox.value()
        self.ppm_tolletance = self.ui.ppm_spinbox.value()
        self.da_tolletance = self.ui.dalton_spinbox.value()
        if self.search_mode == 'ppm':
            self.search_property = ['ppm', self.ui.ppm_spinbox.value()]
        else:
            self.search_property = ['dalton', self.ui.dalton_spinbox.value()]

        if (self.ui.DB_line.text() and self.ui.SP_line.text()) != "":
            FilesList = []

            for CurrentFile in self.files.glob("*.csv"):
                FilesList.append(CurrentFile)
            search_peak(FilesList, self.DB_path, self.addotti, self.carica,
                        self.search_property, self.addotti_label, Filtering=self.filterValues)
            print('Complete :-)')
        else:
            QtWidgets.QMessageBox.warning(self, "Warning", "Input files are missing")          
'''
def main():
    # a new app instance
    app = QtWidgets.QApplication(sys.argv)
    window = Ui()
    window.setWindowTitle("MASS_CIRCUS - v3.0")
    # without this, the script exits immediately.
    sys.exit(app.exec_())


if __name__ == "__main__":
    main()