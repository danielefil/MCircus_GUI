
from PyQt5 import QtCore, QtGui, QtWidgets, uic
from PyQt5.QtWidgets import QDialog, QMainWindow, QApplication, QFileDialog
from pathlib import Path


import sys
import csv
from element import Element
from FormulaFinder_lib import FormulaFinder, FormulaRefiner

class Ui(QtWidgets.QMainWindow):
    def __init__(self):   
        super(Ui, self).__init__() # Call the inherited classes __init__ method
        uic.loadUi('Dialog_FormulaFinder.ui', self) # Load the .ui file
        self.show()
        # INIT FUNCTIONS
        self.tmpfiles = []
        self.tableWidget.horizontalHeader().setSectionResizeMode(QtWidgets.QHeaderView.Stretch)
        self.EC_Open_btn.clicked.connect(self.openElementalComp_Dialog)
        self.Refine_GBox.setEnabled(False)
        self.IsoFinder_GBox.setEnabled(False)
        self.Search_btn.clicked.connect(self.findCompoundList)
        self.Refine_btn.clicked.connect(self.refineCompoundList)
        self.IsoFind_btn.clicked.connect(self.PatternFinder)
        self.Option_GBox.setEnabled(False)
        #for debug
        self.spectralist = [r'C:\Users\df426\Desktop\AnalisiCromo\Spectra\Part2_2020_7_3_cromoacetato_gallico_1a3_h2o_meoh_1a100_400-2000_NEG.csv']
    

    def readTableData(self):
        rowCount = self.tableWidget.rowCount()
        columnCount =  self.tableWidget.columnCount()
        output = []
        for row in range(rowCount):
            rowlist = []
            for column in range(columnCount):
                CellItem = self.tableWidget.item(row, column)
                if (CellItem and CellItem.text):
                    if column == 0:
                        rowlist.append(CellItem.text()) 
                    elif column == 1:
                        rowlist.append(float(CellItem.text())) 
                    else:
                        rowlist.append(int(CellItem.text())) 
            output.append(rowlist)
        return(output)



        
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
                for i in mylist[0]:
                    element = Element(i, 1)
                    rowPosition = self.tableWidget.rowCount()
                    self.tableWidget.insertRow(rowPosition)    
                    self.tableWidget.setItem(rowPosition, 0, QtWidgets.QTableWidgetItem(str(element.symbol)))
                    self.tableWidget.setItem(rowPosition, 1, QtWidgets.QTableWidgetItem(str(round(element.iso_molecular_weight,5))))
                    self.tableWidget.setItem(rowPosition, 2, QtWidgets.QTableWidgetItem(str(1)))
                    self.tableWidget.setItem(rowPosition, 3, QtWidgets.QTableWidgetItem(str(0)))
        
        self.tableWidget.sortItems(1, order = QtCore.Qt.DescendingOrder)
        self.Option_GBox.setEnabled(True)


    def findCompoundList(self):
        self.Search_LB.setText('')
        tmp_path = (Path(__file__).parent).joinpath('tmp') 
        try:
            tmp_path.mkdir(parents=True, exist_ok=True)
        except FileExistsError:
            pass
        
        out = []
        spectra = []
        if not(self.Pos_RBtn.isChecked() or self.Neg_RBtn.isChecked()):
            QtWidgets.QMessageBox.warning(self, "Warning", "Select spectra Charge to continue")
        else:
            if self.Pos_RBtn.isChecked():
                self.charge = int(self.charge_cBox.currentText())
            if self.Neg_RBtn.isChecked():
                self.charge = -int(self.charge_cBox.currentText())
            ppm_diff = self.ppm_SPbox.value()
            atoms = self.readTableData()
            
            for spectra in self.spectralist:
                out = FormulaFinder(spectra, atoms, self.charge, ppm_diff, out)
                out.to_csv(str(tmp_path)+ '/' + str(Path(spectra).name), index=False)
                self.tmpfiles.append(str(tmp_path)+ '/' + str(Path(spectra).name))
            self.Search_LB.setText('Done !!')
            self.Refine_GBox.setEnabled(True)


    def refineCompoundList(self):
        self.tmpfiles_2 = []
        self.selectFilter()
        for _file in self.tmpfiles:
            Complist = FormulaRefiner(_file, self.charge, self.ratios)
            self.tmpfiles_2.append(Complist)
        self.Refine_LB.setText('Done !!')
        self.IsoFinder_GBox.setEnabled(True)


    def selectFilter(self):
        self.ratios = {}
        if self.DBE_CBox.isChecked():
            self.ratios['DBE'] = (self.DBE_min_SBox.value(), self.DBE_max_SBox.value())
        if self.HC_CBox.isChecked():
            self.ratios['H'] = (self.HC_min_SBox.value(), self.HC_max_SBox.value())
        if self.OC_CBox.isChecked():
            self.ratios['O'] = (self.OC_min_SBox.value(), self.OC_max_SBox.value())


    def PatternFinder(self):
        if not(self.ppm_RBtn.isChecked() or self.dalton_RBtn.isChecked()):
            QtWidgets.QMessageBox.warning(self, "Warning", "Select ppm or dalton mode")
        else:
            if self.ppm_RBtn.isChecked():
                SearchMode = 'ppm'
            if self.dalton_RBtn.isChecked():
                SearchMode = 'dalton'
     
            ppm = self.ppm_SPbox_2.value()
            dalton = self.dalton_SPbox.value()
            #for spettro, composti in zip(self.spectra, self.tmpfiles2): 
                #IsoFinder()
            print(ppm, dalton, self.charge, SearchMode)


def main():
    # a new app instance
    app = QtWidgets.QApplication(sys.argv)
    window = Ui()
    window.setWindowTitle("MASS_CIRCUS - v7.0")
    # without this, the script exits immediately.
    sys.exit(app.exec_())


if __name__ == "__main__":
    main()