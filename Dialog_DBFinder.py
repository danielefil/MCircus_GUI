from PyQt5 import QtWidgets, uic
from PyQt5.QtWidgets import QDialog, QApplication, QFileDialog
from PatternSearch_lib import PatternSearch


class PatternOptionsDialog(QDialog):
    def __init__(self, OptionsList, parent = None):   
        super(PatternOptionsDialog, self).__init__(parent) # Call the inherited classes __init__ method
        uic.loadUi('Dialog_PatternOptions.ui', self) # Load the .ui file
        self.setWindowTitle("Isotopic pattern Options")
        #self.show()

        # INIT GLOBAL VARIABLES AND OPTIONS
        self.optionsList = OptionsList

        #CONNECTION
        self.SetOptions_btn.toggled.connect(self.SetOptions)
        self.MinIntensity = self.MinInt_SBox.value()
        self.MergeThre = self.MergeThreshold_SBox.value()
        self.IntensityRation = self.IntensityRation_SBox.value()

    def SetOptions(self):
        #self.OptionsList = [self.MinIntensity, self.MergeThre, self.IntensityRation]
        #print('cioa')
        self.close()
        #return(self.OptionsList)



class Ui(QDialog):
    def __init__(self, FileList, FilterOptions, parent = None):   
        super(Ui, self).__init__(parent) # Call the inherited classes __init__ method
        uic.loadUi("Dialog_ListFinder.ui", self) # Load the .ui file
        self.setWindowTitle("Compound List Finder")
        self.show()
        
        # INIT GLOBAL VARIABLES AND OPTIONS
        self.SpectraList = FileList
        self.FilterProperty = FilterOptions
        self.PatternOptions = [.00001, .0005, .001]
        #DISABLED
        self.Adducts_GBox.setEnabled(False)
        self.Charge_GBox.setEnabled(False)
        self.DB_Create_btn.setEnabled(False)
        self.IsoFinder_GBox.setEnabled(False)
        self.Positive_gBox.setEnabled(False)
        self.Negative_GBox.setEnabled(False)

        #CONNECTION
        self.DB_Open_btn.clicked.connect(self.openDatabase_Dialog)
        self.Positive_RBtn.toggled.connect(self.Enable_Adducts_Selector)
        self.Negative_RBtn.toggled.connect(self.Enable_Adducts_Selector)
        self.DB_Create_btn.clicked.connect(self.Adducts_generator)
        self.IsoFind_btn.clicked.connect(self.PatternFinder)
        self.IsoOptions_btn.clicked.connect(self.Pattern_Options)
    
    # OPEN FILES DIALOG -- COMPOUNDS LIST FILE
    def openDatabase_Dialog(self):
        options = QFileDialog.Options()
        options |= QFileDialog.DontUseNativeDialog
        files, _ = QFileDialog.getOpenFileNames(self, "Select Compounds List file", "", "DAT Files (*.dat);;Text Files (*.txt)", options=options)
        if files:
            self.DB_line.setText(files[0])
            self.DB_path = files[0]
            self.Adducts_GBox.setEnabled(True)
        #print(self.DB_path) # FOR DEBUG
    
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
    
    # ADDUCT LIST CREATOR   
    def Adducts_generator(self):
        if self.Positive_RBtn.isChecked():
            self.pos_adducts_generator()
        else:
            self.neg_adducts_generator()
        
        #print(self.charge, self.adducts, self.adducts_label) #FOR DEBUG
        # MESSAGGIO OPERAZIONE COMPLETATA
        QtWidgets.QMessageBox.about(self, "Message", "Adducts list Created")
        self.IsoFinder_GBox.setEnabled(True)

    # NEGATIVE ADDUCT LIST CREATOR
    def neg_adducts_generator(self):
        self.adducts = []
        self.adducts_label = []
        if self.Mneg_cBtn.isChecked():
            self.adducts.append("El")
            self.adducts_label.append("(-)")
        if self.Formate_cBtn.isChecked():
            self.adducts.append("HCOO")
            self.adducts_label.append("+fo(-)")
        if self.Acetate_cBtn.isChecked():
            self.adducts.append("C2H3O2")
            self.adducts_label.append("+ac(-)")
        if self.Cloride_cBtn.isChecked():
            self.adducts.append("Cl")
            self.adducts_label.append("+Cl(-)")
        if self.DeProton_cBtn.isChecked():
            self.adducts.append("Hp")
            self.adducts_label.append("-H(+)")
        self.charge = -int(self.charge_number_comboBox.currentText())


    # POSITIVE ADDUCT LIST CREATOR
    def pos_adducts_generator(self):
        self.adducts = []
        self.adducts_label = []
        if self.Mpos_cBtn.isChecked():
            self.adducts.append("El")
            self.adducts_label.append("(+)")
        if self.Potassium_cBtn.isChecked():
            self.adducts.append("K")
            self.adducts_label.append("+K(+)")
        if self.Sodium_cBtn.isChecked():
            self.adducts.append("Na")
            self.adducts_label.append("+Na(+)")
        if self.Ammonium_cBtn.isChecked():
            self.adducts.append("NH4")
            self.adducts_label.append("+am(+)")
        if self.Proton_cBtn.isChecked():
            self.adducts.append("H")
            self.adducts_label.append("+H(+)")
        self.charge = int(self.charge_number_comboBox.currentText())

    def Pattern_Options(self):
        dlg = PatternOptionsDialog(self.PatternOptions)
        #dlg.exec()
        
        print(dlg.SetOptions())
    
    # PPM/DALTON SELECTION AND ISOTOPIC PATTERN SEARCH
    def PatternFinder(self):
        if not(self.ppm_RBtn.isChecked() or self.dalton_RBtn.isChecked()):
            QtWidgets.QMessageBox.warning(self, "Warning", "Select ppm or dalton mode")
        else:
            if self.ppm_RBtn.isChecked():
                SearchMode = 'ppm'
                ppm = self.ppm_SPbox.value()
                search_property = [SearchMode, ppm]
            if self.dalton_RBtn.isChecked():
                SearchMode = 'dalton'
                dalton = self.dalton_SPbox.value()
                search_property = [SearchMode, dalton]
    
            ##### ###### LOOP WITH PROGRESS BAR TO SEARCH COMPOUDS WITH ISOTOPIC PATTERN MATCH ###### #######  
            self.IsoFinder_PBar.reset()
            self.IsoFinder_PBar.setMaximum(len(self.SpectraList))
            self.IsoFind_btn.setEnabled(False)
            for index, _spectra in enumerate(self.SpectraList, 1):
                self.IsoFinder_PBar.setValue(index)
                QApplication.processEvents()
                PatternSearch(_spectra, self.DB_path, self.adducts, self.charge,  search_property, self.adducts_label, self.FilterProperty, self.PatternOptions)
            QtWidgets.QMessageBox.information(self, "Info", "Analysis completed!")
            self.IsoFinder_PBar.reset()
            self.IsoFind_btn.setEnabled(True)