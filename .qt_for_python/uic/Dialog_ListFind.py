# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'c:\Users\df426\Documents\MCircus_GUI\Dialog_ListFind.ui'
#
# Created by: PyQt5 UI code generator 5.15.4
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Dialog(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(840, 435)
        self.groupBox_2 = QtWidgets.QGroupBox(Dialog)
        self.groupBox_2.setGeometry(QtCore.QRect(40, 120, 761, 171))
        self.groupBox_2.setObjectName("groupBox_2")
        self.Positive_radio = QtWidgets.QRadioButton(self.groupBox_2)
        self.Positive_radio.setGeometry(QtCore.QRect(10, 50, 141, 17))
        self.Positive_radio.setObjectName("Positive_radio")
        self.Negative_radio = QtWidgets.QRadioButton(self.groupBox_2)
        self.Negative_radio.setGeometry(QtCore.QRect(10, 120, 141, 17))
        self.Negative_radio.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.Negative_radio.setAutoFillBackground(False)
        self.Negative_radio.setObjectName("Negative_radio")
        self.verticalLayoutWidget_2 = QtWidgets.QWidget(self.groupBox_2)
        self.verticalLayoutWidget_2.setGeometry(QtCore.QRect(150, 20, 501, 141))
        self.verticalLayoutWidget_2.setObjectName("verticalLayoutWidget_2")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(self.verticalLayoutWidget_2)
        self.verticalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.gBPositive = QtWidgets.QGroupBox(self.verticalLayoutWidget_2)
        self.gBPositive.setEnabled(True)
        self.gBPositive.setAlignment(QtCore.Qt.AlignCenter)
        self.gBPositive.setObjectName("gBPositive")
        self.horizontalLayoutWidget = QtWidgets.QWidget(self.gBPositive)
        self.horizontalLayoutWidget.setGeometry(QtCore.QRect(0, 20, 501, 31))
        self.horizontalLayoutWidget.setObjectName("horizontalLayoutWidget")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.horizontalLayoutWidget)
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.cBProtone = QtWidgets.QCheckBox(self.horizontalLayoutWidget)
        self.cBProtone.setObjectName("cBProtone")
        self.horizontalLayout.addWidget(self.cBProtone)
        self.cBSodio = QtWidgets.QCheckBox(self.horizontalLayoutWidget)
        self.cBSodio.setObjectName("cBSodio")
        self.horizontalLayout.addWidget(self.cBSodio)
        self.cBPotassio = QtWidgets.QCheckBox(self.horizontalLayoutWidget)
        self.cBPotassio.setObjectName("cBPotassio")
        self.horizontalLayout.addWidget(self.cBPotassio)
        self.cBAmmonio = QtWidgets.QCheckBox(self.horizontalLayoutWidget)
        self.cBAmmonio.setObjectName("cBAmmonio")
        self.horizontalLayout.addWidget(self.cBAmmonio)
        self.verticalLayout_2.addWidget(self.gBPositive)
        self.gBNegative = QtWidgets.QGroupBox(self.verticalLayoutWidget_2)
        self.gBNegative.setEnabled(True)
        self.gBNegative.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.gBNegative.setAlignment(QtCore.Qt.AlignCenter)
        self.gBNegative.setCheckable(False)
        self.gBNegative.setObjectName("gBNegative")
        self.horizontalLayoutWidget_2 = QtWidgets.QWidget(self.gBNegative)
        self.horizontalLayoutWidget_2.setGeometry(QtCore.QRect(0, 20, 501, 31))
        self.horizontalLayoutWidget_2.setObjectName("horizontalLayoutWidget_2")
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout(self.horizontalLayoutWidget_2)
        self.horizontalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.cBProtone_neg = QtWidgets.QCheckBox(self.horizontalLayoutWidget_2)
        self.cBProtone_neg.setObjectName("cBProtone_neg")
        self.horizontalLayout_2.addWidget(self.cBProtone_neg)
        self.cBCloro = QtWidgets.QCheckBox(self.horizontalLayoutWidget_2)
        self.cBCloro.setObjectName("cBCloro")
        self.horizontalLayout_2.addWidget(self.cBCloro)
        self.cBAcetato = QtWidgets.QCheckBox(self.horizontalLayoutWidget_2)
        self.cBAcetato.setObjectName("cBAcetato")
        self.horizontalLayout_2.addWidget(self.cBAcetato)
        self.cBFormiato = QtWidgets.QCheckBox(self.horizontalLayoutWidget_2)
        self.cBFormiato.setObjectName("cBFormiato")
        self.horizontalLayout_2.addWidget(self.cBFormiato)
        self.verticalLayout_2.addWidget(self.gBNegative)
        self.verticalLayoutWidget_3 = QtWidgets.QWidget(self.groupBox_2)
        self.verticalLayoutWidget_3.setGeometry(QtCore.QRect(660, 100, 92, 61))
        self.verticalLayoutWidget_3.setObjectName("verticalLayoutWidget_3")
        self.verticalLayout_3 = QtWidgets.QVBoxLayout(self.verticalLayoutWidget_3)
        self.verticalLayout_3.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.create_button = QtWidgets.QPushButton(self.verticalLayoutWidget_3)
        self.create_button.setObjectName("create_button")
        self.verticalLayout_3.addWidget(self.create_button)
        self.verticalLayoutWidget_4 = QtWidgets.QWidget(self.groupBox_2)
        self.verticalLayoutWidget_4.setGeometry(QtCore.QRect(660, 20, 92, 61))
        self.verticalLayoutWidget_4.setObjectName("verticalLayoutWidget_4")
        self.verticalLayout_4 = QtWidgets.QVBoxLayout(self.verticalLayoutWidget_4)
        self.verticalLayout_4.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_4.setObjectName("verticalLayout_4")
        self.label_3 = QtWidgets.QLabel(self.verticalLayoutWidget_4)
        self.label_3.setEnabled(True)
        self.label_3.setAlignment(QtCore.Qt.AlignCenter)
        self.label_3.setObjectName("label_3")
        self.verticalLayout_4.addWidget(self.label_3)
        self.charge_number_comboBox = QtWidgets.QComboBox(self.verticalLayoutWidget_4)
        self.charge_number_comboBox.setObjectName("charge_number_comboBox")
        self.charge_number_comboBox.addItem("")
        self.charge_number_comboBox.addItem("")
        self.charge_number_comboBox.addItem("")
        self.charge_number_comboBox.addItem("")
        self.charge_number_comboBox.addItem("")
        self.charge_number_comboBox.addItem("")
        self.charge_number_comboBox.addItem("")
        self.charge_number_comboBox.addItem("")
        self.verticalLayout_4.addWidget(self.charge_number_comboBox)
        self.groupBox_3 = QtWidgets.QGroupBox(Dialog)
        self.groupBox_3.setGeometry(QtCore.QRect(40, 300, 761, 111))
        self.groupBox_3.setObjectName("groupBox_3")
        self.find_button = QtWidgets.QPushButton(self.groupBox_3)
        self.find_button.setGeometry(QtCore.QRect(300, 40, 113, 32))
        self.find_button.setObjectName("find_button")
        self.gridLayoutWidget = QtWidgets.QWidget(self.groupBox_3)
        self.gridLayoutWidget.setGeometry(QtCore.QRect(20, 20, 221, 80))
        self.gridLayoutWidget.setObjectName("gridLayoutWidget")
        self.gridLayout = QtWidgets.QGridLayout(self.gridLayoutWidget)
        self.gridLayout.setContentsMargins(0, 0, 0, 0)
        self.gridLayout.setObjectName("gridLayout")
        self.ppm_radio = QtWidgets.QRadioButton(self.gridLayoutWidget)
        self.ppm_radio.setObjectName("ppm_radio")
        self.gridLayout.addWidget(self.ppm_radio, 0, 0, 1, 1)
        self.ppm_spinbox = QtWidgets.QSpinBox(self.gridLayoutWidget)
        self.ppm_spinbox.setProperty("value", 20)
        self.ppm_spinbox.setObjectName("ppm_spinbox")
        self.gridLayout.addWidget(self.ppm_spinbox, 0, 2, 1, 1)
        self.dalton_radio = QtWidgets.QRadioButton(self.gridLayoutWidget)
        self.dalton_radio.setObjectName("dalton_radio")
        self.gridLayout.addWidget(self.dalton_radio, 1, 0, 1, 1)
        self.dalton_spinbox = QtWidgets.QDoubleSpinBox(self.gridLayoutWidget)
        self.dalton_spinbox.setDecimals(4)
        self.dalton_spinbox.setMinimum(0.0005)
        self.dalton_spinbox.setSingleStep(0.0001)
        self.dalton_spinbox.setObjectName("dalton_spinbox")
        self.gridLayout.addWidget(self.dalton_spinbox, 1, 2, 1, 1)
        spacerItem = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout.addItem(spacerItem, 0, 1, 1, 1)
        spacerItem1 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout.addItem(spacerItem1, 1, 1, 1, 1)
        self.gBox_SearchMethod = QtWidgets.QGroupBox(Dialog)
        self.gBox_SearchMethod.setGeometry(QtCore.QRect(40, 20, 761, 91))
        self.gBox_SearchMethod.setFlat(False)
        self.gBox_SearchMethod.setCheckable(False)
        self.gBox_SearchMethod.setObjectName("gBox_SearchMethod")
        self.gridLayoutWidget_2 = QtWidgets.QWidget(self.gBox_SearchMethod)
        self.gridLayoutWidget_2.setGeometry(QtCore.QRect(10, 20, 741, 61))
        self.gridLayoutWidget_2.setObjectName("gridLayoutWidget_2")
        self.files_selectro_Layout_2 = QtWidgets.QGridLayout(self.gridLayoutWidget_2)
        self.files_selectro_Layout_2.setContentsMargins(0, 0, 0, 0)
        self.files_selectro_Layout_2.setHorizontalSpacing(18)
        self.files_selectro_Layout_2.setVerticalSpacing(6)
        self.files_selectro_Layout_2.setObjectName("files_selectro_Layout_2")
        self.DB_Open_btn = QtWidgets.QPushButton(self.gridLayoutWidget_2)
        self.DB_Open_btn.setObjectName("DB_Open_btn")
        self.files_selectro_Layout_2.addWidget(self.DB_Open_btn, 0, 2, 1, 1)
        self.DB_line = QtWidgets.QLineEdit(self.gridLayoutWidget_2)
        self.DB_line.setObjectName("DB_line")
        self.files_selectro_Layout_2.addWidget(self.DB_line, 0, 1, 1, 1)
        self.DB_label = QtWidgets.QLabel(self.gridLayoutWidget_2)
        self.DB_label.setObjectName("DB_label")
        self.files_selectro_Layout_2.addWidget(self.DB_label, 0, 0, 1, 1)

        self.retranslateUi(Dialog)
        self.charge_number_comboBox.setCurrentIndex(0)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "Dialog"))
        self.groupBox_2.setTitle(_translate("Dialog", "Adducts selector"))
        self.Positive_radio.setText(_translate("Dialog", "Positive Spectra"))
        self.Negative_radio.setText(_translate("Dialog", "Negative Spectra"))
        self.gBPositive.setTitle(_translate("Dialog", "Positive Adducts"))
        self.cBProtone.setText(_translate("Dialog", "Proton (H+)"))
        self.cBSodio.setText(_translate("Dialog", "Sodium (Na+)"))
        self.cBPotassio.setText(_translate("Dialog", "Potassium (K+)"))
        self.cBAmmonio.setText(_translate("Dialog", "Ammoniun (NH4+)"))
        self.gBNegative.setTitle(_translate("Dialog", "Negative Adducts"))
        self.cBProtone_neg.setText(_translate("Dialog", "Proton -(H+)"))
        self.cBCloro.setText(_translate("Dialog", "Cloride (Cl-)"))
        self.cBAcetato.setText(_translate("Dialog", "Acetate (CH3COO−)"))
        self.cBFormiato.setText(_translate("Dialog", "Formate (HCOO-)"))
        self.create_button.setText(_translate("Dialog", "CREATE"))
        self.label_3.setText(_translate("Dialog", "Max charge"))
        self.charge_number_comboBox.setItemText(0, _translate("Dialog", "1"))
        self.charge_number_comboBox.setItemText(1, _translate("Dialog", "2"))
        self.charge_number_comboBox.setItemText(2, _translate("Dialog", "3"))
        self.charge_number_comboBox.setItemText(3, _translate("Dialog", "4"))
        self.charge_number_comboBox.setItemText(4, _translate("Dialog", "5"))
        self.charge_number_comboBox.setItemText(5, _translate("Dialog", "6"))
        self.charge_number_comboBox.setItemText(6, _translate("Dialog", "7"))
        self.charge_number_comboBox.setItemText(7, _translate("Dialog", "8"))
        self.groupBox_3.setTitle(_translate("Dialog", "Finder"))
        self.find_button.setText(_translate("Dialog", "Find"))
        self.ppm_radio.setText(_translate("Dialog", "ppm Difference"))
        self.dalton_radio.setText(_translate("Dialog", "Dalton Difference"))
        self.gBox_SearchMethod.setTitle(_translate("Dialog", "Compounds list file"))
        self.DB_Open_btn.setText(_translate("Dialog", "Open"))
        self.DB_label.setText(_translate("Dialog", "File Path"))
