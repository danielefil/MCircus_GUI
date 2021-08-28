from PyQt5 import QtCore, QtGui, QtWidgets, uic
from PyQt5.QtWidgets import QDialog, QMainWindow, QApplication, QFileDialog
from pathlib import Path
import sys
import csv
from element import Element


class Ui(QDialog):
    def __init__(self, FileList, parent = None):   
        super(Ui, self).__init__(parent) # Call the inherited classes __init__ method
        uic.loadUi("Dialog_ListFinder.ui", self) # Load the .ui file
        self.setWindowTitle("Compound List Finder")
        self.show()
        
        #DISABLED
        self.Adducts_GBox.setEnabled(False)
        self.Charge_GBox.setEnabled(False)
        self.DB_Create_btn.setEnabled(False)
        self.Finder_GBox.setEnabled(False)
        self.Positive_gBox.setEnabled(False)
        self.Negative_GBox.setEnabled(False)


        #CONNECTION
        self.DB_Open_btn.clicked.connect(self.openDatabase_Dialog)
        self.Positive_RBtn.toggled.connect(self.Enable_Adducts_Selector)
        self.Negative_RBtn.toggled.connect(self.Enable_Adducts_Selector)
        self.ppm_RBtn.toggled.connect(self.Enable_Finder_Selector)
        self.dalton_RBtn.toggled.connect(self.Enable_Finder_Selector)
        self.DB_Create_btn.clicked.connect(self.Adducts_generator)
        #self.find_button.clicked.connect(self.finder)
    
    def openDatabase_Dialog(self):
        options = QFileDialog.Options()
        options |= QFileDialog.DontUseNativeDialog
        files, _ = QFileDialog.getOpenFileNames(self, "Select Compounds List file", "", "CSV Files (*.csv);;Text Files (*.txt)", options=options)
        if files:
            self.DB_line.setText(files[0])
            self.DB_path = files[0]
            self.Adducts_GBox.setEnabled(True)
        print(self.DB_path) # FRO DEBUG
    
    # ENABLE/DISABLE +/- ADDUCTOR SELECTOR
    def Enable_Adducts_Selector(self):
        if self.Positive_RBtn.isChecked():
            self.Positive_gBox.setEnabled(True)
            self.Negative_GBox.setEnabled(False)
            self.DB_Create_btn.setEnabled(True)
            self.Charge_GBox.setEnabled(True)
        else:
            self.Positive_gBox.setEnabled(False)
            self.Negative_GBox.setEnabled(True)
            self.DB_Create_btn.setEnabled(True)
            self.Charge_GBox.setEnabled(True)

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

        
    def Adducts_generator(self):
        if self.Positive_RBtn.isChecked():
            self.pos_adducts_generator()
        else:
            self.neg_adducts_generator()

        # NEGATIVE ADDUCT LIST CREATOR
    def neg_adducts_creator(self):
        self.addotti = []
        self.addotti_label = []
        if self.ui.Mneg_cBtn.isChecked():
            self.addotti.append("El")
            self.addotti_label.append("(-)")
        if self.ui.Formiate_cBtn.isChecked():
            self.addotti.append("HCOO")
            self.addotti_label.append("+fo(-)")
        if self.ui.Acetate_cBtn.isChecked():
            self.addotti.append("C2H3O2")
            self.addotti_label.append("+ac(-)")
        if self.ui.Cloride_cBtn.isChecked():
            self.addotti.append("Cl")
            self.addotti_label.append("+Cl(-)")
        if self.ui.DeProton_cBtn.isChecked():
            self.addotti.append("Hp")
            self.addotti_label.append("-H(+)")
        self.carica = -int(self.ui.charge_number_comboBox.currentText())
        # MESSAGGIO OPERAZIONE COMPLETATA
        QtWidgets.QMessageBox.about(self, "Message", "Adducts list Created")

        # POSITIVE ADDUCT LIST CREATOR
    def pos_adducts_generator(self):
        self.addotti = []
        self.addotti_label = []
        if self.ui.Mpos_cBtn.isChecked():
            self.addotti.append("El")
            self.addotti_label.append("(+)")
        if self.ui.Potassium_cBtn.isChecked():
            self.addotti.append("K")
            self.addotti_label.append("+K(+)")
        if self.ui.Sodium_cBtn.isChecked():
            self.addotti.append("Na")
            self.addotti_label.append("+Na(+)")
        if self.ui.Ammonium_cBtn.isChecked():
            self.addotti.append("NH4")
            self.addotti_label.append("+am(+)")
        if self.ui.Proton_cBtn.isChecked():
            self.addotti.append("H")
            self.addotti_label.append("+H(+)")
        self.carica = int(self.ui.charge_number_comboBox.currentText())
        # MESSAGGIO OPERAZIONE COMPLETATA
        QtWidgets.QMessageBox.about(self, "Message", "Adducts list Created")


