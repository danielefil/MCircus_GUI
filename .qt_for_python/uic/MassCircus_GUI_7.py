# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'c:\Users\df426\Documents\MCircus_GUI\MassCircus_GUI_7.ui'
#
# Created by: PyQt5 UI code generator 5.15.4
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(470, 400)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.tabWidget = QtWidgets.QTabWidget(self.centralwidget)
        self.tabWidget.setGeometry(QtCore.QRect(10, 10, 450, 370))
        self.tabWidget.setObjectName("tabWidget")
        self.tab_1 = QtWidgets.QWidget()
        self.tab_1.setObjectName("tab_1")
        self.groupBox = QtWidgets.QGroupBox(self.tab_1)
        self.groupBox.setGeometry(QtCore.QRect(10, 10, 420, 190))
        self.groupBox.setFlat(False)
        self.groupBox.setCheckable(False)
        self.groupBox.setObjectName("groupBox")
        self.gridLayoutWidget = QtWidgets.QWidget(self.groupBox)
        self.gridLayoutWidget.setGeometry(QtCore.QRect(20, 80, 381, 71))
        self.gridLayoutWidget.setObjectName("gridLayoutWidget")
        self.files_selectro_Layout = QtWidgets.QGridLayout(self.gridLayoutWidget)
        self.files_selectro_Layout.setContentsMargins(0, 0, 0, 0)
        self.files_selectro_Layout.setHorizontalSpacing(5)
        self.files_selectro_Layout.setVerticalSpacing(0)
        self.files_selectro_Layout.setObjectName("files_selectro_Layout")
        self.OpenSP_btn = QtWidgets.QPushButton(self.gridLayoutWidget)
        self.OpenSP_btn.setObjectName("OpenSP_btn")
        self.files_selectro_Layout.addWidget(self.OpenSP_btn, 1, 2, 1, 1)
        self.SP_line = QtWidgets.QLineEdit(self.gridLayoutWidget)
        self.SP_line.setObjectName("SP_line")
        self.files_selectro_Layout.addWidget(self.SP_line, 1, 1, 1, 1)
        self.SP_label = QtWidgets.QLabel(self.gridLayoutWidget)
        self.SP_label.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.SP_label.setFrameShadow(QtWidgets.QFrame.Plain)
        self.SP_label.setScaledContents(False)
        self.SP_label.setAlignment(QtCore.Qt.AlignCenter)
        self.SP_label.setObjectName("SP_label")
        self.files_selectro_Layout.addWidget(self.SP_label, 0, 1, 1, 1)
        self.gridLayoutWidget_3 = QtWidgets.QWidget(self.groupBox)
        self.gridLayoutWidget_3.setGeometry(QtCore.QRect(20, 30, 381, 31))
        self.gridLayoutWidget_3.setObjectName("gridLayoutWidget_3")
        self.gridLayout = QtWidgets.QGridLayout(self.gridLayoutWidget_3)
        self.gridLayout.setContentsMargins(0, 0, 0, 0)
        self.gridLayout.setObjectName("gridLayout")
        self.raw_rdbtn = QtWidgets.QRadioButton(self.gridLayoutWidget_3)
        self.raw_rdbtn.setObjectName("raw_rdbtn")
        self.gridLayout.addWidget(self.raw_rdbtn, 0, 2, 1, 1)
        self.mzML_rdbtn = QtWidgets.QRadioButton(self.gridLayoutWidget_3)
        self.mzML_rdbtn.setObjectName("mzML_rdbtn")
        self.gridLayout.addWidget(self.mzML_rdbtn, 0, 3, 1, 1)
        self.csv_rdbtn = QtWidgets.QRadioButton(self.gridLayoutWidget_3)
        self.csv_rdbtn.setObjectName("csv_rdbtn")
        self.gridLayout.addWidget(self.csv_rdbtn, 0, 1, 1, 1)
        self.FileExtension_Label = QtWidgets.QLabel(self.gridLayoutWidget_3)
        self.FileExtension_Label.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.FileExtension_Label.setFrameShadow(QtWidgets.QFrame.Plain)
        self.FileExtension_Label.setScaledContents(False)
        self.FileExtension_Label.setAlignment(QtCore.Qt.AlignCenter)
        self.FileExtension_Label.setObjectName("FileExtension_Label")
        self.gridLayout.addWidget(self.FileExtension_Label, 0, 0, 1, 1)
        self.Next1_btn = QtWidgets.QPushButton(self.tab_1)
        self.Next1_btn.setGeometry(QtCore.QRect(355, 210, 75, 25))
        self.Next1_btn.setObjectName("Next1_btn")
        self.tabWidget.addTab(self.tab_1, "")
        self.tab_2 = QtWidgets.QWidget()
        self.tab_2.setObjectName("tab_2")
        self.gBox_Filter = QtWidgets.QGroupBox(self.tab_2)
        self.gBox_Filter.setGeometry(QtCore.QRect(10, 10, 420, 190))
        self.gBox_Filter.setObjectName("gBox_Filter")
        self.EnableFilter_cbtn = QtWidgets.QCheckBox(self.gBox_Filter)
        self.EnableFilter_cbtn.setGeometry(QtCore.QRect(150, 20, 141, 20))
        self.EnableFilter_cbtn.setObjectName("EnableFilter_cbtn")
        self.gBox_NoiseFilter = QtWidgets.QGroupBox(self.gBox_Filter)
        self.gBox_NoiseFilter.setGeometry(QtCore.QRect(10, 50, 401, 131))
        self.gBox_NoiseFilter.setTitle("")
        self.gBox_NoiseFilter.setObjectName("gBox_NoiseFilter")
        self.gridLayoutWidget_2 = QtWidgets.QWidget(self.gBox_NoiseFilter)
        self.gridLayoutWidget_2.setGeometry(QtCore.QRect(10, 10, 381, 101))
        self.gridLayoutWidget_2.setObjectName("gridLayoutWidget_2")
        self.gridLayout_2 = QtWidgets.QGridLayout(self.gridLayoutWidget_2)
        self.gridLayout_2.setContentsMargins(0, 0, 0, 0)
        self.gridLayout_2.setObjectName("gridLayout_2")
        self.BreakCount_spinbox = QtWidgets.QSpinBox(self.gridLayoutWidget_2)
        self.BreakCount_spinbox.setMaximum(300)
        self.BreakCount_spinbox.setProperty("value", 200)
        self.BreakCount_spinbox.setObjectName("BreakCount_spinbox")
        self.gridLayout_2.addWidget(self.BreakCount_spinbox, 1, 2, 1, 1)
        self.label_2 = QtWidgets.QLabel(self.gridLayoutWidget_2)
        self.label_2.setObjectName("label_2")
        self.gridLayout_2.addWidget(self.label_2, 1, 0, 1, 1)
        self.IntensePerc_spinbox = QtWidgets.QDoubleSpinBox(self.gridLayoutWidget_2)
        self.IntensePerc_spinbox.setMaximum(1.0)
        self.IntensePerc_spinbox.setSingleStep(0.05)
        self.IntensePerc_spinbox.setProperty("value", 0.8)
        self.IntensePerc_spinbox.setObjectName("IntensePerc_spinbox")
        self.gridLayout_2.addWidget(self.IntensePerc_spinbox, 0, 2, 1, 1)
        self.label = QtWidgets.QLabel(self.gridLayoutWidget_2)
        self.label.setObjectName("label")
        self.gridLayout_2.addWidget(self.label, 0, 0, 1, 1)
        spacerItem = QtWidgets.QSpacerItem(90, 20, QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout_2.addItem(spacerItem, 0, 1, 1, 1)
        self.Next2_btn = QtWidgets.QPushButton(self.tab_2)
        self.Next2_btn.setGeometry(QtCore.QRect(355, 210, 75, 25))
        self.Next2_btn.setObjectName("Next2_btn")
        self.tabWidget.addTab(self.tab_2, "")
        self.tab_3 = QtWidgets.QWidget()
        self.tab_3.setObjectName("tab_3")
        self.gBox_SearchMethod = QtWidgets.QGroupBox(self.tab_3)
        self.gBox_SearchMethod.setGeometry(QtCore.QRect(10, 10, 420, 190))
        self.gBox_SearchMethod.setFlat(False)
        self.gBox_SearchMethod.setCheckable(False)
        self.gBox_SearchMethod.setObjectName("gBox_SearchMethod")
        self.EC_Dialog_btn = QtWidgets.QPushButton(self.gBox_SearchMethod)
        self.EC_Dialog_btn.setGeometry(QtCore.QRect(30, 60, 150, 50))
        self.EC_Dialog_btn.setObjectName("EC_Dialog_btn")
        self.DB_Dialog_btn = QtWidgets.QPushButton(self.gBox_SearchMethod)
        self.DB_Dialog_btn.setGeometry(QtCore.QRect(240, 60, 150, 50))
        self.DB_Dialog_btn.setObjectName("DB_Dialog_btn")
        self.tabWidget.addTab(self.tab_3, "")
        MainWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        self.tabWidget.setCurrentIndex(0)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.groupBox.setTitle(_translate("MainWindow", "Open file"))
        self.OpenSP_btn.setText(_translate("MainWindow", "Open"))
        self.SP_label.setText(_translate("MainWindow", "Spectrum Folder"))
        self.raw_rdbtn.setText(_translate("MainWindow", "*.raw"))
        self.mzML_rdbtn.setText(_translate("MainWindow", "*.mzML"))
        self.csv_rdbtn.setText(_translate("MainWindow", "*.csv"))
        self.FileExtension_Label.setText(_translate("MainWindow", "File extension"))
        self.Next1_btn.setText(_translate("MainWindow", "Next"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_1), _translate("MainWindow", "Input"))
        self.gBox_Filter.setTitle(_translate("MainWindow", "Filter"))
        self.EnableFilter_cbtn.setText(_translate("MainWindow", "Enable Filtering"))
        self.label_2.setText(_translate("MainWindow", "Break Count"))
        self.label.setText(_translate("MainWindow", "Max Intensity Percentile"))
        self.Next2_btn.setText(_translate("MainWindow", "Next"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_2), _translate("MainWindow", "Noise Filter"))
        self.gBox_SearchMethod.setTitle(_translate("MainWindow", "Search method"))
        self.EC_Dialog_btn.setText(_translate("MainWindow", "Elemental Composition"))
        self.DB_Dialog_btn.setText(_translate("MainWindow", "Compounds List"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_3), _translate("MainWindow", "Find method"))
