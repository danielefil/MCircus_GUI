# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file "c:\Users\df426\Documents\MCircus_GUI\Dialog_FormulaFinder2.ui"
#
# Created by: PyQt5 UI code generator 5.15.4
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Dialog(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(781, 711)
        self.IsoFinder_GBox = QtWidgets.QGroupBox(Dialog)
        self.IsoFinder_GBox.setGeometry(QtCore.QRect(10, 610, 761, 91))
        self.IsoFinder_GBox.setObjectName("IsoFinder_GBox")
        self.IsoFind_btn = QtWidgets.QPushButton(self.IsoFinder_GBox)
        self.IsoFind_btn.setGeometry(QtCore.QRect(510, 30, 141, 41))
        self.IsoFind_btn.setObjectName("IsoFind_btn")
        self.dalton_SPbox = QtWidgets.QDoubleSpinBox(self.IsoFinder_GBox)
        self.dalton_SPbox.setGeometry(QtCore.QRect(170, 60, 91, 21))
        self.dalton_SPbox.setDecimals(4)
        self.dalton_SPbox.setMinimum(0.0005)
        self.dalton_SPbox.setSingleStep(0.0001)
        self.dalton_SPbox.setObjectName("dalton_SPbox")
        self.ppm_SPbox_2 = QtWidgets.QSpinBox(self.IsoFinder_GBox)
        self.ppm_SPbox_2.setGeometry(QtCore.QRect(170, 30, 91, 21))
        self.ppm_SPbox_2.setProperty("value", 20)
        self.ppm_SPbox_2.setObjectName("ppm_SPbox_2")
        self.ppm_RBtn = QtWidgets.QRadioButton(self.IsoFinder_GBox)
        self.ppm_RBtn.setGeometry(QtCore.QRect(10, 30, 141, 17))
        self.ppm_RBtn.setObjectName("ppm_RBtn")
        self.dalton_RBtn = QtWidgets.QRadioButton(self.IsoFinder_GBox)
        self.dalton_RBtn.setGeometry(QtCore.QRect(10, 60, 151, 17))
        self.dalton_RBtn.setObjectName("dalton_RBtn")
        self.groupBox_2 = QtWidgets.QGroupBox(Dialog)
        self.groupBox_2.setGeometry(QtCore.QRect(10, 120, 760, 301))
        self.groupBox_2.setObjectName("groupBox_2")
        self.Option_GBox = QtWidgets.QGroupBox(self.groupBox_2)
        self.Option_GBox.setGeometry(QtCore.QRect(390, 20, 365, 270))
        self.Option_GBox.setObjectName("Option_GBox")
        self.Pos_RBtn = QtWidgets.QRadioButton(self.Option_GBox)
        self.Pos_RBtn.setGeometry(QtCore.QRect(50, 30, 141, 17))
        self.Pos_RBtn.setObjectName("Pos_RBtn")
        self.Neg_RBtn = QtWidgets.QRadioButton(self.Option_GBox)
        self.Neg_RBtn.setGeometry(QtCore.QRect(210, 30, 141, 17))
        self.Neg_RBtn.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.Neg_RBtn.setAutoFillBackground(False)
        self.Neg_RBtn.setObjectName("Neg_RBtn")
        self.ppm_SPbox = QtWidgets.QSpinBox(self.Option_GBox)
        self.ppm_SPbox.setGeometry(QtCore.QRect(220, 110, 81, 31))
        self.ppm_SPbox.setProperty("value", 10)
        self.ppm_SPbox.setObjectName("ppm_SPbox")
        self.Search_btn = QtWidgets.QPushButton(self.Option_GBox)
        self.Search_btn.setGeometry(QtCore.QRect(120, 170, 141, 41))
        self.Search_btn.setObjectName("Search_btn")
        self.charge_cBox = QtWidgets.QComboBox(self.Option_GBox)
        self.charge_cBox.setGeometry(QtCore.QRect(220, 69, 80, 31))
        self.charge_cBox.setMaxCount(5)
        self.charge_cBox.setObjectName("charge_cBox")
        self.charge_cBox.addItem("")
        self.charge_cBox.addItem("")
        self.charge_cBox.addItem("")
        self.charge_cBox.addItem("")
        self.charge_cBox.addItem("")
        self.label = QtWidgets.QLabel(self.Option_GBox)
        self.label.setGeometry(QtCore.QRect(30, 70, 101, 20))
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(self.Option_GBox)
        self.label_2.setGeometry(QtCore.QRect(30, 120, 101, 20))
        self.label_2.setObjectName("label_2")
        self.Search_LB = QtWidgets.QLabel(self.Option_GBox)
        self.Search_LB.setGeometry(QtCore.QRect(120, 220, 141, 31))
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.Search_LB.setFont(font)
        self.Search_LB.setText("")
        self.Search_LB.setAlignment(QtCore.Qt.AlignCenter)
        self.Search_LB.setObjectName("Search_LB")
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
        self.gBox_SearchMethod = QtWidgets.QGroupBox(Dialog)
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
        self.Refine_GBox = QtWidgets.QGroupBox(Dialog)
        self.Refine_GBox.setGeometry(QtCore.QRect(10, 440, 761, 161))
        self.Refine_GBox.setObjectName("Refine_GBox")
        self.gridLayoutWidget = QtWidgets.QWidget(self.Refine_GBox)
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
        self.Refine_btn = QtWidgets.QPushButton(self.Refine_GBox)
        self.Refine_btn.setGeometry(QtCore.QRect(510, 60, 141, 41))
        self.Refine_btn.setObjectName("Refine_btn")
        self.Refine_LB = QtWidgets.QLabel(self.Refine_GBox)
        self.Refine_LB.setGeometry(QtCore.QRect(510, 110, 141, 31))
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.Refine_LB.setFont(font)
        self.Refine_LB.setText("")
        self.Refine_LB.setAlignment(QtCore.Qt.AlignCenter)
        self.Refine_LB.setObjectName("Refine_LB")

        self.retranslateUi(Dialog)
        self.charge_cBox.setCurrentIndex(0)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "Dialog"))
        self.IsoFinder_GBox.setTitle(_translate("Dialog", "Finder"))
        self.IsoFind_btn.setText(_translate("Dialog", "Find"))
        self.ppm_RBtn.setText(_translate("Dialog", "ppm Difference"))
        self.dalton_RBtn.setText(_translate("Dialog", "Dalton Difference"))
        self.groupBox_2.setTitle(_translate("Dialog", "Properties"))
        self.Option_GBox.setTitle(_translate("Dialog", "Search Options"))
        self.Pos_RBtn.setText(_translate("Dialog", "Positive Spectra"))
        self.Neg_RBtn.setText(_translate("Dialog", "Negative Spectra"))
        self.Search_btn.setText(_translate("Dialog", "Find"))
        self.charge_cBox.setItemText(0, _translate("Dialog", "1"))
        self.charge_cBox.setItemText(1, _translate("Dialog", "2"))
        self.charge_cBox.setItemText(2, _translate("Dialog", "3"))
        self.charge_cBox.setItemText(3, _translate("Dialog", "4"))
        self.charge_cBox.setItemText(4, _translate("Dialog", "5"))
        self.label.setText(_translate("Dialog", "Max Charge"))
        self.label_2.setText(_translate("Dialog", "ppm Difference"))
        self.groupBox_4.setTitle(_translate("Dialog", "Search Elements"))
        item = self.tableWidget.horizontalHeaderItem(0)
        item.setText(_translate("Dialog", "Element"))
        item = self.tableWidget.horizontalHeaderItem(1)
        item.setText(_translate("Dialog", "MM"))
        item = self.tableWidget.horizontalHeaderItem(2)
        item.setText(_translate("Dialog", "Min"))
        item = self.tableWidget.horizontalHeaderItem(3)
        item.setText(_translate("Dialog", "Max"))
        self.gBox_SearchMethod.setTitle(_translate("Dialog", "Compounds list file"))
        self.EC_Open_btn.setText(_translate("Dialog", "Open"))
        self.EC_label.setText(_translate("Dialog", "Elements file"))
        self.Refine_GBox.setTitle(_translate("Dialog", "Refine"))
        self.DBE_CBox.setText(_translate("Dialog", "DBE "))
        self.OC_CBox.setText(_translate("Dialog", "O/C"))
        self.HC_CBox.setText(_translate("Dialog", "H/C"))
        self.Refine_btn.setText(_translate("Dialog", "Refine"))
