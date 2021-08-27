from PyQt5 import QtCore, QtGui, QtWidgets, uic
from PyQt5.QtWidgets import QDialog, QMainWindow, QApplication, QFileDialog
from pathlib import Path
import sys
import csv
from element import Element
from FormulaFinder_lib import FormulaFinder, FormulaRefiner


class Ui(QDialog):
    def __init__(self, FileList, parent = None):   
        super(Ui, self).__init__(parent) # Call the inherited classes __init__ method
        uic.loadUi('Dialog_ListFinder.ui', self) # Load the .ui file
        self.setWindowTitle("Compound List Finder")
        self.show()
        
        #DISABLED
        self.Adducts_gBox.setEnabled(False)
        self.Charge_GBox.setEnabled(False)
        self.DB_Create_btn.setEnabled(False)
        self.Finder_GBox.setEnabled(False)


        #CONNECTION
        self.DB_Open_btn.clicked.connect(self.openDatabase_Dialog)
        self.Positive_RBtn.toggled.connect(self.Enable_Adducts_Selector)
        self.Negative_RBtn.toggled.connect(self.Enable_Adducts_Selector)
        self.ppm_RBtn.toggled.connect(self.Enable_Finder_Selector)
        self.dalton_RBtn.toggled.connect(self.Enable_Finder_Selector)
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

