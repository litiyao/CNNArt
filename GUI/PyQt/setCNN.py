# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'setCNN.ui'
#
# Created by: PyQt5 UI code generator 5.6
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_setCNN(object):
    def setupUi(self, setCNN):
        setCNN.setObjectName("setCNN")
        setCNN.resize(477, 755)
        self.centralwidget = QtWidgets.QWidget(setCNN)
        self.centralwidget.setObjectName("centralwidget")
        self.start = QtWidgets.QPushButton(self.centralwidget)
        self.start.setGeometry(QtCore.QRect(310, 610, 111, 31))
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.start.setFont(font)
        self.start.setObjectName("start")
        self.progressBar = QtWidgets.QProgressBar(self.centralwidget)
        self.progressBar.setGeometry(QtCore.QRect(20, 660, 441, 31))
        self.progressBar.setProperty("value", 24)
        self.progressBar.setObjectName("progressBar")
        self.gridLayoutWidget = QtWidgets.QWidget(self.centralwidget)
        self.gridLayoutWidget.setGeometry(QtCore.QRect(30, 120, 391, 461))
        self.gridLayoutWidget.setObjectName("gridLayoutWidget")
        self.gridLayout = QtWidgets.QGridLayout(self.gridLayoutWidget)
        self.gridLayout.setContentsMargins(0, 0, 0, 0)
        self.gridLayout.setObjectName("gridLayout")
        self.label_3 = QtWidgets.QLabel(self.gridLayoutWidget)
        self.label_3.setObjectName("label_3")
        self.gridLayout.addWidget(self.label_3, 1, 0, 1, 1)
        self.comboBox_4 = QtWidgets.QComboBox(self.gridLayoutWidget)
        self.comboBox_4.setObjectName("comboBox_4")
        self.gridLayout.addWidget(self.comboBox_4, 3, 1, 1, 1)
        self.label_6 = QtWidgets.QLabel(self.gridLayoutWidget)
        self.label_6.setObjectName("label_6")
        self.gridLayout.addWidget(self.label_6, 4, 0, 1, 1)
        self.label_5 = QtWidgets.QLabel(self.gridLayoutWidget)
        self.label_5.setObjectName("label_5")
        self.gridLayout.addWidget(self.label_5, 3, 0, 1, 1)
        self.comboBox = QtWidgets.QComboBox(self.gridLayoutWidget)
        self.comboBox.setObjectName("comboBox")
        self.gridLayout.addWidget(self.comboBox, 0, 1, 1, 1)
        self.comboBox_2 = QtWidgets.QComboBox(self.gridLayoutWidget)
        self.comboBox_2.setObjectName("comboBox_2")
        self.gridLayout.addWidget(self.comboBox_2, 1, 1, 1, 1)
        self.label = QtWidgets.QLabel(self.gridLayoutWidget)
        self.label.setObjectName("label")
        self.gridLayout.addWidget(self.label, 0, 0, 1, 1)
        self.comboBox_6 = QtWidgets.QComboBox(self.gridLayoutWidget)
        self.comboBox_6.setObjectName("comboBox_6")
        self.gridLayout.addWidget(self.comboBox_6, 5, 1, 1, 1)
        self.label_7 = QtWidgets.QLabel(self.gridLayoutWidget)
        self.label_7.setObjectName("label_7")
        self.gridLayout.addWidget(self.label_7, 5, 0, 1, 1)
        self.label_4 = QtWidgets.QLabel(self.gridLayoutWidget)
        self.label_4.setObjectName("label_4")
        self.gridLayout.addWidget(self.label_4, 2, 0, 1, 1)
        self.comboBox_3 = QtWidgets.QComboBox(self.gridLayoutWidget)
        self.comboBox_3.setObjectName("comboBox_3")
        self.gridLayout.addWidget(self.comboBox_3, 2, 1, 1, 1)
        self.comboBox_5 = QtWidgets.QComboBox(self.gridLayoutWidget)
        self.comboBox_5.setObjectName("comboBox_5")
        self.gridLayout.addWidget(self.comboBox_5, 4, 1, 1, 1)
        self.pushButton = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton.setGeometry(QtCore.QRect(30, 20, 93, 28))
        self.pushButton.setObjectName("pushButton")
        self.datapath = QtWidgets.QTextBrowser(self.centralwidget)
        self.datapath.setGeometry(QtCore.QRect(30, 60, 391, 31))
        self.datapath.setObjectName("datapath")
        setCNN.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(setCNN)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 477, 26))
        self.menubar.setObjectName("menubar")
        setCNN.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(setCNN)
        self.statusbar.setObjectName("statusbar")
        setCNN.setStatusBar(self.statusbar)

        self.retranslateUi(setCNN)
        QtCore.QMetaObject.connectSlotsByName(setCNN)

    def retranslateUi(self, setCNN):
        _translate = QtCore.QCoreApplication.translate
        setCNN.setWindowTitle(_translate("setCNN", "CNN setting"))
        self.start.setText(_translate("setCNN", "Start Training"))
        self.label_3.setText(_translate("setCNN", "Parameter Optimization"))
        self.label_6.setText(_translate("setCNN", "Epoch"))
        self.label_5.setText(_translate("setCNN", "Learning Rate"))
        self.label.setText(_translate("setCNN", "CNN Model"))
        self.label_7.setText(_translate("setCNN", "CNN method"))
        self.label_4.setText(_translate("setCNN", "Batch Size"))
        self.pushButton.setText(_translate("setCNN", "Choose Path"))
