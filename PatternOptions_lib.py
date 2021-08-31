from PyQt5 import QtCore, QtWidgets, uic
from PyQt5.QtWidgets import QDialog, QApplication, QFileDialog

class Ui(QDialog):
    def __init__(self, parent = None):   
        super(Ui, self).__init__(parent) # Call the inherited classes __init__ method
        uic.loadUi('Dialog_PatternOptions.ui', self) # Load the .ui file
        self.setWindowTitle("Isotopic Pattern Calculator Options")
        self.show()