from PyQt5 import uic
from PyQt5.QtWidgets import QDialog



class Ui(QDialog):
    def __init__(self, OptionsList, parent = None):   
        super(Ui, self).__init__(parent) # Call the inherited classes __init__ method
        uic.loadUi("Ui/Dialog_PatternOptions.ui", self) # Load the .ui file
        self.setWindowTitle("Isotopic pattern Options")

        # INIT GLOBAL VARIABLES AND OPTIONS
        self.optionsList = OptionsList
        self.MinInt_SBox.setValue(OptionsList[0])
        self.MergeThreshold_SBox.setValue(OptionsList[1])
        self.IntensityRation_SBox.setValue(OptionsList[2])

        #CONNECTION
        self.SetOptions_btn.clicked.connect(self.SetOptions)

    def SetOptions(self):
        self.optionsList = [self.MinInt_SBox.value(), self.MergeThreshold_SBox.value(), self.IntensityRation_SBox.value()]
        self.close()
        return(self.optionsList)