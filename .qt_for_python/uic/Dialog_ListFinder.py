# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file "c:\Users\df426\Documents\MCircus_GUI\Ui\Dialog_ListFinder.ui"
#
# Created by: PyQt5 UI code generator 5.15.4
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Dialog(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(781, 457)
        self.Adducts_GBox = QtWidgets.QGroupBox(Dialog)
        self.Adducts_GBox.setGeometry(QtCore.QRect(10, 110, 761, 171))
        self.Adducts_GBox.setObjectName("Adducts_GBox")
        self.Positive_RBtn = QtWidgets.QRadioButton(self.Adducts_GBox)
        self.Positive_RBtn.setGeometry(QtCore.QRect(10, 50, 141, 17))
        self.Positive_RBtn.setObjectName("Positive_RBtn")
        self.Negative_RBtn = QtWidgets.QRadioButton(self.Adducts_GBox)
        self.Negative_RBtn.setGeometry(QtCore.QRect(10, 120, 141, 17))
        self.Negative_RBtn.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.Negative_RBtn.setAutoFillBackground(False)
        self.Negative_RBtn.setObjectName("Negative_RBtn")
        self.verticalLayoutWidget_2 = QtWidgets.QWidget(self.Adducts_GBox)
        self.verticalLayoutWidget_2.setGeometry(QtCore.QRect(90, 20, 561, 141))
        self.verticalLayoutWidget_2.setObjectName("verticalLayoutWidget_2")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(self.verticalLayoutWidget_2)
        self.verticalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.Positive_gBox = QtWidgets.QGroupBox(self.verticalLayoutWidget_2)
        self.Positive_gBox.setEnabled(True)
        self.Positive_gBox.setAlignment(QtCore.Qt.AlignCenter)
        self.Positive_gBox.setObjectName("Positive_gBox")
        self.gridLayoutWidget_3 = QtWidgets.QWidget(self.Positive_gBox)
        self.gridLayoutWidget_3.setGeometry(QtCore.QRect(0, 20, 561, 41))
        self.gridLayoutWidget_3.setObjectName("gridLayoutWidget_3")
        self.gridLayout_2 = QtWidgets.QGridLayout(self.gridLayoutWidget_3)
        self.gridLayout_2.setContentsMargins(0, 0, 0, 0)
        self.gridLayout_2.setObjectName("gridLayout_2")
        self.Potassium_cBtn = QtWidgets.QCheckBox(self.gridLayoutWidget_3)
        self.Potassium_cBtn.setObjectName("Potassium_cBtn")
        self.gridLayout_2.addWidget(self.Potassium_cBtn, 0, 3, 1, 1)
        self.Ammonium_cBtn = QtWidgets.QCheckBox(self.gridLayoutWidget_3)
        self.Ammonium_cBtn.setObjectName("Ammonium_cBtn")
        self.gridLayout_2.addWidget(self.Ammonium_cBtn, 0, 4, 1, 1)
        self.Mpos_cBtn = QtWidgets.QCheckBox(self.gridLayoutWidget_3)
        self.Mpos_cBtn.setObjectName("Mpos_cBtn")
        self.gridLayout_2.addWidget(self.Mpos_cBtn, 0, 0, 1, 1)
        self.Proton_cBtn = QtWidgets.QCheckBox(self.gridLayoutWidget_3)
        self.Proton_cBtn.setObjectName("Proton_cBtn")
        self.gridLayout_2.addWidget(self.Proton_cBtn, 0, 1, 1, 1)
        self.Sodium_cBtn = QtWidgets.QCheckBox(self.gridLayoutWidget_3)
        self.Sodium_cBtn.setObjectName("Sodium_cBtn")
        self.gridLayout_2.addWidget(self.Sodium_cBtn, 0, 2, 1, 1)
        self.verticalLayout_2.addWidget(self.Positive_gBox)
        self.Negative_GBox = QtWidgets.QGroupBox(self.verticalLayoutWidget_2)
        self.Negative_GBox.setEnabled(True)
        self.Negative_GBox.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.Negative_GBox.setAlignment(QtCore.Qt.AlignCenter)
        self.Negative_GBox.setCheckable(False)
        self.Negative_GBox.setObjectName("Negative_GBox")
        self.gridLayoutWidget_4 = QtWidgets.QWidget(self.Negative_GBox)
        self.gridLayoutWidget_4.setGeometry(QtCore.QRect(0, 20, 561, 41))
        self.gridLayoutWidget_4.setObjectName("gridLayoutWidget_4")
        self.gridLayout_4 = QtWidgets.QGridLayout(self.gridLayoutWidget_4)
        self.gridLayout_4.setSizeConstraint(QtWidgets.QLayout.SetMinimumSize)
        self.gridLayout_4.setContentsMargins(0, 0, 0, 0)
        self.gridLayout_4.setObjectName("gridLayout_4")
        self.Mneg_cBtn = QtWidgets.QCheckBox(self.gridLayoutWidget_4)
        self.Mneg_cBtn.setObjectName("Mneg_cBtn")
        self.gridLayout_4.addWidget(self.Mneg_cBtn, 0, 0, 1, 1)
        self.Acetate_cBtn = QtWidgets.QCheckBox(self.gridLayoutWidget_4)
        self.Acetate_cBtn.setObjectName("Acetate_cBtn")
        self.gridLayout_4.addWidget(self.Acetate_cBtn, 0, 3, 1, 1)
        self.DeProton_cBtn = QtWidgets.QCheckBox(self.gridLayoutWidget_4)
        self.DeProton_cBtn.setObjectName("DeProton_cBtn")
        self.gridLayout_4.addWidget(self.DeProton_cBtn, 0, 1, 1, 1)
        self.Cloride_cBtn = QtWidgets.QCheckBox(self.gridLayoutWidget_4)
        self.Cloride_cBtn.setObjectName("Cloride_cBtn")
        self.gridLayout_4.addWidget(self.Cloride_cBtn, 0, 2, 1, 1)
        self.Formate_cBtn = QtWidgets.QCheckBox(self.gridLayoutWidget_4)
        self.Formate_cBtn.setObjectName("Formate_cBtn")
        self.gridLayout_4.addWidget(self.Formate_cBtn, 0, 4, 1, 1)
        self.verticalLayout_2.addWidget(self.Negative_GBox)
        self.verticalLayoutWidget_3 = QtWidgets.QWidget(self.Adducts_GBox)
        self.verticalLayoutWidget_3.setGeometry(QtCore.QRect(660, 100, 92, 61))
        self.verticalLayoutWidget_3.setObjectName("verticalLayoutWidget_3")
        self.verticalLayout_3 = QtWidgets.QVBoxLayout(self.verticalLayoutWidget_3)
        self.verticalLayout_3.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.DB_Create_btn = QtWidgets.QPushButton(self.verticalLayoutWidget_3)
        self.DB_Create_btn.setObjectName("DB_Create_btn")
        self.verticalLayout_3.addWidget(self.DB_Create_btn)
        self.IsoFinder_GBox = QtWidgets.QGroupBox(Dialog)
        self.IsoFinder_GBox.setGeometry(QtCore.QRect(10, 290, 761, 131))
        self.IsoFinder_GBox.setObjectName("IsoFinder_GBox")
        self.IsoFind_btn = QtWidgets.QPushButton(self.IsoFinder_GBox)
        self.IsoFind_btn.setGeometry(QtCore.QRect(430, 40, 113, 32))
        self.IsoFind_btn.setObjectName("IsoFind_btn")
        self.gridLayoutWidget = QtWidgets.QWidget(self.IsoFinder_GBox)
        self.gridLayoutWidget.setGeometry(QtCore.QRect(10, 20, 261, 101))
        self.gridLayoutWidget.setObjectName("gridLayoutWidget")
        self.gridLayout = QtWidgets.QGridLayout(self.gridLayoutWidget)
        self.gridLayout.setContentsMargins(0, 0, 0, 0)
        self.gridLayout.setObjectName("gridLayout")
        spacerItem = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout.addItem(spacerItem, 2, 1, 1, 1)
        self.dalton_SPbox = QtWidgets.QDoubleSpinBox(self.gridLayoutWidget)
        self.dalton_SPbox.setDecimals(4)
        self.dalton_SPbox.setMinimum(0.0005)
        self.dalton_SPbox.setSingleStep(0.0001)
        self.dalton_SPbox.setObjectName("dalton_SPbox")
        self.gridLayout.addWidget(self.dalton_SPbox, 2, 2, 1, 1)
        spacerItem1 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout.addItem(spacerItem1, 1, 1, 1, 1)
        self.dalton_RBtn = QtWidgets.QRadioButton(self.gridLayoutWidget)
        self.dalton_RBtn.setObjectName("dalton_RBtn")
        self.gridLayout.addWidget(self.dalton_RBtn, 2, 0, 1, 1)
        self.ppm_RBtn = QtWidgets.QRadioButton(self.gridLayoutWidget)
        self.ppm_RBtn.setObjectName("ppm_RBtn")
        self.gridLayout.addWidget(self.ppm_RBtn, 1, 0, 1, 1)
        self.ppm_SPbox = QtWidgets.QSpinBox(self.gridLayoutWidget)
        self.ppm_SPbox.setProperty("value", 20)
        self.ppm_SPbox.setObjectName("ppm_SPbox")
        self.gridLayout.addWidget(self.ppm_SPbox, 1, 2, 1, 1)
        self.IsoOptions_btn = QtWidgets.QPushButton(self.gridLayoutWidget)
        self.IsoOptions_btn.setObjectName("IsoOptions_btn")
        self.gridLayout.addWidget(self.IsoOptions_btn, 0, 0, 1, 1)
        self.IsoFinder_PBar = QtWidgets.QProgressBar(self.IsoFinder_GBox)
        self.IsoFinder_PBar.setGeometry(QtCore.QRect(340, 80, 291, 16))
        self.IsoFinder_PBar.setProperty("value", 0)
        self.IsoFinder_PBar.setObjectName("IsoFinder_PBar")
        self.gBox_SearchMethod = QtWidgets.QGroupBox(Dialog)
        self.gBox_SearchMethod.setGeometry(QtCore.QRect(10, 10, 761, 91))
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
        self.Charge_GBox = QtWidgets.QGroupBox(Dialog)
        self.Charge_GBox.setEnabled(True)
        self.Charge_GBox.setGeometry(QtCore.QRect(670, 130, 90, 70))
        self.Charge_GBox.setAlignment(QtCore.Qt.AlignCenter)
        self.Charge_GBox.setObjectName("Charge_GBox")
        self.charge_number_comboBox = QtWidgets.QComboBox(self.Charge_GBox)
        self.charge_number_comboBox.setGeometry(QtCore.QRect(5, 30, 80, 20))
        self.charge_number_comboBox.setMaxCount(5)
        self.charge_number_comboBox.setObjectName("charge_number_comboBox")
        self.charge_number_comboBox.addItem("")
        self.charge_number_comboBox.addItem("")
        self.charge_number_comboBox.addItem("")
        self.charge_number_comboBox.addItem("")
        self.charge_number_comboBox.addItem("")

        self.retranslateUi(Dialog)
        self.charge_number_comboBox.setCurrentIndex(0)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "Dialog"))
        self.Adducts_GBox.setTitle(_translate("Dialog", "Adducts selector"))
        self.Positive_RBtn.setText(_translate("Dialog", "Positive"))
        self.Negative_RBtn.setText(_translate("Dialog", "Negative"))
        self.Positive_gBox.setTitle(_translate("Dialog", "Positive Adducts"))
        self.Potassium_cBtn.setText(_translate("Dialog", "Potassium (K+)"))
        self.Ammonium_cBtn.setText(_translate("Dialog", "Ammoniun (NH4+)"))
        self.Mpos_cBtn.setText(_translate("Dialog", "M+"))
        self.Proton_cBtn.setText(_translate("Dialog", "Proton (H+)"))
        self.Sodium_cBtn.setText(_translate("Dialog", "Sodium (Na+)"))
        self.Negative_GBox.setTitle(_translate("Dialog", "Negative Adducts"))
        self.Mneg_cBtn.setText(_translate("Dialog", "M-"))
        self.Acetate_cBtn.setText(_translate("Dialog", "Acetate (CH3COO−)"))
        self.DeProton_cBtn.setText(_translate("Dialog", "Proton -(H+)"))
        self.Cloride_cBtn.setText(_translate("Dialog", "Cloride (Cl-)"))
        self.Formate_cBtn.setText(_translate("Dialog", "Formate (HCOO-)"))
        self.DB_Create_btn.setText(_translate("Dialog", "CREATE"))
        self.IsoFinder_GBox.setTitle(_translate("Dialog", "Finder"))
        self.IsoFind_btn.setText(_translate("Dialog", "Find"))
        self.dalton_RBtn.setText(_translate("Dialog", "Dalton Difference"))
        self.ppm_RBtn.setText(_translate("Dialog", "ppm Difference"))
        self.IsoOptions_btn.setText(_translate("Dialog", "Iso Pattern Options"))
        self.gBox_SearchMethod.setTitle(_translate("Dialog", "Compounds list file"))
        self.DB_Open_btn.setText(_translate("Dialog", "Open"))
        self.DB_label.setText(_translate("Dialog", "File Path"))
        self.Charge_GBox.setTitle(_translate("Dialog", "Max Charge"))
        self.charge_number_comboBox.setItemText(0, _translate("Dialog", "1"))
        self.charge_number_comboBox.setItemText(1, _translate("Dialog", "2"))
        self.charge_number_comboBox.setItemText(2, _translate("Dialog", "3"))
        self.charge_number_comboBox.setItemText(3, _translate("Dialog", "4"))
        self.charge_number_comboBox.setItemText(4, _translate("Dialog", "5"))
