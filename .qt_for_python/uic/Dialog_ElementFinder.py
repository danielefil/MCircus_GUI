# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file "c:\Users\df426\Documents\MCircus_GUI\ElemFind Dialog\Dialog_ElementFinder.ui"
#
# Created by: PyQt5 UI code generator 5.15.4
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(781, 729)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.groupBox_2 = QtWidgets.QGroupBox(self.centralwidget)
        self.groupBox_2.setGeometry(QtCore.QRect(10, 120, 760, 301))
        self.groupBox_2.setObjectName("groupBox_2")
        self.gBox_Option = QtWidgets.QGroupBox(self.groupBox_2)
        self.gBox_Option.setGeometry(QtCore.QRect(390, 20, 365, 270))
        self.gBox_Option.setObjectName("gBox_Option")
        self.Pos_RBtn = QtWidgets.QRadioButton(self.gBox_Option)
        self.Pos_RBtn.setGeometry(QtCore.QRect(50, 30, 141, 17))
        self.Pos_RBtn.setObjectName("Pos_RBtn")
        self.Neg_RBtn = QtWidgets.QRadioButton(self.gBox_Option)
        self.Neg_RBtn.setGeometry(QtCore.QRect(210, 30, 141, 17))
        self.Neg_RBtn.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.Neg_RBtn.setAutoFillBackground(False)
        self.Neg_RBtn.setObjectName("Neg_RBtn")
        self.ppm_SPbox = QtWidgets.QSpinBox(self.gBox_Option)
        self.ppm_SPbox.setGeometry(QtCore.QRect(220, 110, 81, 31))
        self.ppm_SPbox.setProperty("value", 10)
        self.ppm_SPbox.setObjectName("ppm_SPbox")
        self.Search_btn = QtWidgets.QPushButton(self.gBox_Option)
        self.Search_btn.setGeometry(QtCore.QRect(120, 170, 141, 41))
        self.Search_btn.setObjectName("Search_btn")
        self.charge_cBox = QtWidgets.QComboBox(self.gBox_Option)
        self.charge_cBox.setGeometry(QtCore.QRect(220, 69, 80, 31))
        self.charge_cBox.setMaxCount(5)
        self.charge_cBox.setObjectName("charge_cBox")
        self.charge_cBox.addItem("")
        self.charge_cBox.addItem("")
        self.charge_cBox.addItem("")
        self.charge_cBox.addItem("")
        self.charge_cBox.addItem("")
        self.label = QtWidgets.QLabel(self.gBox_Option)
        self.label.setGeometry(QtCore.QRect(30, 70, 101, 20))
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(self.gBox_Option)
        self.label_2.setGeometry(QtCore.QRect(30, 120, 101, 20))
        self.label_2.setObjectName("label_2")
        self.progressBar = QtWidgets.QProgressBar(self.gBox_Option)
        self.progressBar.setGeometry(QtCore.QRect(20, 230, 321, 23))
        self.progressBar.setProperty("value", 0)
        self.progressBar.setTextVisible(False)
        self.progressBar.setObjectName("progressBar")
        self.groupBox_4 = QtWidgets.QGroupBox(self.groupBox_2)
        self.groupBox_4.setGeometry(QtCore.QRect(10, 20, 365, 270))
        self.groupBox_4.setObjectName("groupBox_4")
        self.tableWidget = QtWidgets.QTableWidget(self.groupBox_4)
        self.tableWidget.setGeometry(QtCore.QRect(10, 30, 341, 231))
        self.tableWidget.setAutoFillBackground(False)
        self.tableWidget.setObjectName("tableWidget")
        self.tableWidget.setColumnCount(4)
        self.tableWidget.setRowCount(0)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(1, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(2, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(3, item)
        self.tableWidget.horizontalHeader().setCascadingSectionResizes(False)
        self.tableWidget.horizontalHeader().setDefaultSectionSize(75)
        self.tableWidget.horizontalHeader().setStretchLastSection(False)
        self.tableWidget.verticalHeader().setStretchLastSection(False)
        self.gBox_SearchMethod = QtWidgets.QGroupBox(self.centralwidget)
        self.gBox_SearchMethod.setGeometry(QtCore.QRect(10, 10, 761, 91))
        self.gBox_SearchMethod.setFlat(False)
        self.gBox_SearchMethod.setCheckable(False)
        self.gBox_SearchMethod.setObjectName("gBox_SearchMethod")
        self.gridLayoutWidget_4 = QtWidgets.QWidget(self.gBox_SearchMethod)
        self.gridLayoutWidget_4.setGeometry(QtCore.QRect(10, 20, 741, 61))
        self.gridLayoutWidget_4.setObjectName("gridLayoutWidget_4")
        self.files_selectro_Layout_3 = QtWidgets.QGridLayout(self.gridLayoutWidget_4)
        self.files_selectro_Layout_3.setContentsMargins(0, 0, 0, 0)
        self.files_selectro_Layout_3.setHorizontalSpacing(18)
        self.files_selectro_Layout_3.setVerticalSpacing(6)
        self.files_selectro_Layout_3.setObjectName("files_selectro_Layout_3")
        self.EC_Open_btn = QtWidgets.QPushButton(self.gridLayoutWidget_4)
        self.EC_Open_btn.setObjectName("EC_Open_btn")
        self.files_selectro_Layout_3.addWidget(self.EC_Open_btn, 0, 2, 1, 1)
        self.EC_line = QtWidgets.QLineEdit(self.gridLayoutWidget_4)
        self.EC_line.setObjectName("EC_line")
        self.files_selectro_Layout_3.addWidget(self.EC_line, 0, 1, 1, 1)
        self.EC_label = QtWidgets.QLabel(self.gridLayoutWidget_4)
        self.EC_label.setObjectName("EC_label")
        self.files_selectro_Layout_3.addWidget(self.EC_label, 0, 0, 1, 1)
        self.groupBox_6 = QtWidgets.QGroupBox(self.centralwidget)
        self.groupBox_6.setGeometry(QtCore.QRect(10, 440, 761, 161))
        self.groupBox_6.setObjectName("groupBox_6")
        self.gridLayoutWidget = QtWidgets.QWidget(self.groupBox_6)
        self.gridLayoutWidget.setGeometry(QtCore.QRect(10, 20, 351, 126))
        self.gridLayoutWidget.setObjectName("gridLayoutWidget")
        self.gridLayout = QtWidgets.QGridLayout(self.gridLayoutWidget)
        self.gridLayout.setContentsMargins(0, 0, 0, 0)
        self.gridLayout.setObjectName("gridLayout")
        self.DBE_CBox = QtWidgets.QCheckBox(self.gridLayoutWidget)
        self.DBE_CBox.setObjectName("DBE_CBox")
        self.gridLayout.addWidget(self.DBE_CBox, 0, 0, 1, 1)
        self.OC_max_SBox = QtWidgets.QSpinBox(self.gridLayoutWidget)
        self.OC_max_SBox.setProperty("value", 5)
        self.OC_max_SBox.setObjectName("OC_max_SBox")
        self.gridLayout.addWidget(self.OC_max_SBox, 2, 3, 1, 1)
        self.DBE_min_SBox = QtWidgets.QSpinBox(self.gridLayoutWidget)
        self.DBE_min_SBox.setFrame(True)
        self.DBE_min_SBox.setProperty("value", 0)
        self.DBE_min_SBox.setObjectName("DBE_min_SBox")
        self.gridLayout.addWidget(self.DBE_min_SBox, 0, 1, 1, 1)
        self.DBE_max_SBox = QtWidgets.QSpinBox(self.gridLayoutWidget)
        self.DBE_max_SBox.setProperty("value", 5)
        self.DBE_max_SBox.setObjectName("DBE_max_SBox")
        self.gridLayout.addWidget(self.DBE_max_SBox, 0, 3, 1, 1)
        self.HC_min_SBox = QtWidgets.QSpinBox(self.gridLayoutWidget)
        self.HC_min_SBox.setProperty("value", 0)
        self.HC_min_SBox.setObjectName("HC_min_SBox")
        self.gridLayout.addWidget(self.HC_min_SBox, 1, 1, 1, 1)
        self.HC_max_SBox = QtWidgets.QSpinBox(self.gridLayoutWidget)
        self.HC_max_SBox.setProperty("value", 5)
        self.HC_max_SBox.setObjectName("HC_max_SBox")
        self.gridLayout.addWidget(self.HC_max_SBox, 1, 3, 1, 1)
        self.OC_min_SBox = QtWidgets.QSpinBox(self.gridLayoutWidget)
        self.OC_min_SBox.setProperty("value", 0)
        self.OC_min_SBox.setObjectName("OC_min_SBox")
        self.gridLayout.addWidget(self.OC_min_SBox, 2, 1, 1, 1)
        self.OC_CBox = QtWidgets.QCheckBox(self.gridLayoutWidget)
        self.OC_CBox.setObjectName("OC_CBox")
        self.gridLayout.addWidget(self.OC_CBox, 2, 0, 1, 1)
        self.HC_CBox = QtWidgets.QCheckBox(self.gridLayoutWidget)
        self.HC_CBox.setObjectName("HC_CBox")
        self.gridLayout.addWidget(self.HC_CBox, 1, 0, 1, 1)
        spacerItem = QtWidgets.QSpacerItem(60, 20, QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout.addItem(spacerItem, 0, 2, 1, 1)
        self.Refine_btn = QtWidgets.QPushButton(self.groupBox_6)
        self.Refine_btn.setGeometry(QtCore.QRect(510, 60, 141, 41))
        self.Refine_btn.setObjectName("Refine_btn")
        self.groupBox_3 = QtWidgets.QGroupBox(self.centralwidget)
        self.groupBox_3.setGeometry(QtCore.QRect(10, 610, 761, 91))
        self.groupBox_3.setObjectName("groupBox_3")
        self.Isofind_btn = QtWidgets.QPushButton(self.groupBox_3)
        self.Isofind_btn.setGeometry(QtCore.QRect(510, 30, 141, 41))
        self.Isofind_btn.setObjectName("Isofind_btn")
        self.dalton_spinbox = QtWidgets.QDoubleSpinBox(self.groupBox_3)
        self.dalton_spinbox.setGeometry(QtCore.QRect(170, 60, 91, 21))
        self.dalton_spinbox.setDecimals(4)
        self.dalton_spinbox.setMinimum(0.0005)
        self.dalton_spinbox.setSingleStep(0.0001)
        self.dalton_spinbox.setObjectName("dalton_spinbox")
        self.ppm_spinbox = QtWidgets.QSpinBox(self.groupBox_3)
        self.ppm_spinbox.setGeometry(QtCore.QRect(170, 30, 91, 21))
        self.ppm_spinbox.setProperty("value", 20)
        self.ppm_spinbox.setObjectName("ppm_spinbox")
        self.ppm_radio = QtWidgets.QRadioButton(self.groupBox_3)
        self.ppm_radio.setGeometry(QtCore.QRect(10, 30, 141, 17))
        self.ppm_radio.setObjectName("ppm_radio")
        self.dalton_radio = QtWidgets.QRadioButton(self.groupBox_3)
        self.dalton_radio.setGeometry(QtCore.QRect(10, 60, 151, 17))
        self.dalton_radio.setObjectName("dalton_radio")
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)
        self.charge_cBox.setCurrentIndex(0)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.groupBox_2.setTitle(_translate("MainWindow", "Properties"))
        self.gBox_Option.setTitle(_translate("MainWindow", "Search Options"))
        self.Pos_RBtn.setText(_translate("MainWindow", "Positive Spectra"))
        self.Neg_RBtn.setText(_translate("MainWindow", "Negative Spectra"))
        self.Search_btn.setText(_translate("MainWindow", "Find"))
        self.charge_cBox.setItemText(0, _translate("MainWindow", "1"))
        self.charge_cBox.setItemText(1, _translate("MainWindow", "2"))
        self.charge_cBox.setItemText(2, _translate("MainWindow", "3"))
        self.charge_cBox.setItemText(3, _translate("MainWindow", "4"))
        self.charge_cBox.setItemText(4, _translate("MainWindow", "5"))
        self.label.setText(_translate("MainWindow", "Max Charge"))
        self.label_2.setText(_translate("MainWindow", "ppm Difference"))
        self.groupBox_4.setTitle(_translate("MainWindow", "Search Elements"))
        item = self.tableWidget.horizontalHeaderItem(0)
        item.setText(_translate("MainWindow", "Element"))
        item = self.tableWidget.horizontalHeaderItem(1)
        item.setText(_translate("MainWindow", "MM"))
        item = self.tableWidget.horizontalHeaderItem(2)
        item.setText(_translate("MainWindow", "Min"))
        item = self.tableWidget.horizontalHeaderItem(3)
        item.setText(_translate("MainWindow", "Max"))
        self.gBox_SearchMethod.setTitle(_translate("MainWindow", "Compounds list file"))
        self.EC_Open_btn.setText(_translate("MainWindow", "Open"))
        self.EC_label.setText(_translate("MainWindow", "Elements file"))
        self.groupBox_6.setTitle(_translate("MainWindow", "Refine"))
        self.DBE_CBox.setText(_translate("MainWindow", "DBE "))
        self.OC_CBox.setText(_translate("MainWindow", "O/C"))
        self.HC_CBox.setText(_translate("MainWindow", "H/C"))
        self.Refine_btn.setText(_translate("MainWindow", "Refine"))
        self.groupBox_3.setTitle(_translate("MainWindow", "Finder"))
        self.Isofind_btn.setText(_translate("MainWindow", "Find"))
        self.ppm_radio.setText(_translate("MainWindow", "ppm Difference"))
        self.dalton_radio.setText(_translate("MainWindow", "Dalton Difference"))
