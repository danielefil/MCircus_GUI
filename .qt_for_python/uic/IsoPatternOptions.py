# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'c:\Users\df426\Documents\MCircus_GUI\IsoPatternOptions.ui'
#
# Created by: PyQt5 UI code generator 5.15.4
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Dialog(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(354, 126)
        self.gridLayoutWidget = QtWidgets.QWidget(Dialog)
        self.gridLayoutWidget.setGeometry(QtCore.QRect(20, 13, 321, 101))
        self.gridLayoutWidget.setObjectName("gridLayoutWidget")
        self.gridLayout = QtWidgets.QGridLayout(self.gridLayoutWidget)
        self.gridLayout.setContentsMargins(0, 0, 0, 0)
        self.gridLayout.setObjectName("gridLayout")
        self.MinInt_LB = QtWidgets.QLabel(self.gridLayoutWidget)
        self.MinInt_LB.setObjectName("MinInt_LB")
        self.gridLayout.addWidget(self.MinInt_LB, 0, 0, 1, 1)
        self.MinInt_SB = QtWidgets.QDoubleSpinBox(self.gridLayoutWidget)
        self.MinInt_SB.setDecimals(5)
        self.MinInt_SB.setMinimum(1e-05)
        self.MinInt_SB.setMaximum(0.9)
        self.MinInt_SB.setSingleStep(1e-05)
        self.MinInt_SB.setObjectName("MinInt_SB")
        self.gridLayout.addWidget(self.MinInt_SB, 0, 1, 1, 1)
        self.MergeThreshold_LB = QtWidgets.QLabel(self.gridLayoutWidget)
        self.MergeThreshold_LB.setObjectName("MergeThreshold_LB")
        self.gridLayout.addWidget(self.MergeThreshold_LB, 1, 0, 1, 1)
        self.MergeThreshold_SB = QtWidgets.QDoubleSpinBox(self.gridLayoutWidget)
        self.MergeThreshold_SB.setObjectName("MergeThreshold_SB")
        self.gridLayout.addWidget(self.MergeThreshold_SB, 1, 1, 1, 1)
        self.IntRatio_LB = QtWidgets.QLabel(self.gridLayoutWidget)
        self.IntRatio_LB.setObjectName("IntRatio_LB")
        self.gridLayout.addWidget(self.IntRatio_LB, 2, 0, 1, 1)
        self.IntRatio_SB = QtWidgets.QDoubleSpinBox(self.gridLayoutWidget)
        self.IntRatio_SB.setObjectName("IntRatio_SB")
        self.gridLayout.addWidget(self.IntRatio_SB, 2, 1, 1, 1)

        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "Dialog"))
        self.MinInt_LB.setText(_translate("Dialog", "Min Intensity (%)"))
        self.MergeThreshold_LB.setText(_translate("Dialog", "Merge Threshold (dalton)"))
        self.IntRatio_LB.setText(_translate("Dialog", "Intensity Ration (%)"))