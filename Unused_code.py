############# TRASH BIN #############

        #self.adducts = []
        #self.carica = 0

        #self.ppm_tolletance = self.ppm_spinbox.value()
        #self.da_tolletance = self.dalton_spinbox.value()



        ####self.EC_radio.toggled.connect(self.Enable_SearchMtd_Selector)
        ####self.DB_radio.toggled.connect(self.Enable_SearchMtd_Selector)
        ####self.EC_Open_btn.clicked.connect(self.openDataBaseDialog)
        ####self.DB_Open_btn.clicked.connect(self.openDataBaseDialog)
        ####self.Next3_btn.clicked.connect(self.nextTab3_4)
        ####self.Next3_btn.clicked.connect(self.GetSearchMtd)


        #TAB 4 - SEARCH OPTIONS      
        #self.Positive_radio.toggled.connect(self.Enable_Adducts_Selector)
        #self.Negative_radio.toggled.connect(self.Enable_Adducts_Selector)
        #self.ppm_radio.toggled.connect(self.Enable_Finder_Selector)
        #self.dalton_radio.toggled.connect(self.Enable_Finder_Selector)
        #self.create_button.clicked.connect(self.charge_selector)
        #self.openDB_button.clicked.connect(self.openDatabaseDialog)
        #self.find_button.clicked.connect(self.finder)

 
    
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
