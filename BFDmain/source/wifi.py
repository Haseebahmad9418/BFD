# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'wifi.ui'
#
# Created by: PyQt5 UI code generator 5.9.2
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_InitialRegSuccess(object):
    def setupUi(self, InitialRegSuccess):
        InitialRegSuccess.setObjectName("InitialRegSuccess")
        InitialRegSuccess.resize(1044, 620)
        InitialRegSuccess.setStyleSheet("background-color: #F3F4F1;\n"
"QFrame\n"
"{\n"
"    background:#333;\n"
"}")
        self.centralwidget = QtWidgets.QWidget(InitialRegSuccess)
        self.centralwidget.setObjectName("centralwidget")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.centralwidget)
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout.setSpacing(0)
        self.verticalLayout.setObjectName("verticalLayout")
        spacerItem = QtWidgets.QSpacerItem(1041, 6, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout.addItem(spacerItem)
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setSpacing(0)
        self.horizontalLayout.setObjectName("horizontalLayout")
        spacerItem1 = QtWidgets.QSpacerItem(10, 600, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout.addItem(spacerItem1)
        self.frame = QtWidgets.QFrame(self.centralwidget)
        self.frame.setMinimumSize(QtCore.QSize(1024, 600))
        self.frame.setMouseTracking(True)
        self.frame.setStyleSheet("QFrame{\n"
"background:#F3F4F1\n"
"}\n"
"")
        self.frame.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame.setObjectName("frame")
        self.PushButton_2 = QtWidgets.QPushButton(self.frame)
        self.PushButton_2.setGeometry(QtCore.QRect(50, 50, 40, 40))
        self.PushButton_2.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.PushButton_2.setStyleSheet("QPushButton{\n"
"background:#00648E;\n"
"color:white;\n"
"border-color: #00000066;\n"
"border:1px solid #00648E;\n"
"border-radius:5px;\n"
"}")
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("../../BFDmain/source/Icons/ri.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.PushButton_2.setIcon(icon)
        self.PushButton_2.setIconSize(QtCore.QSize(40, 50))
        self.PushButton_2.setObjectName("PushButton_2")
        self.pushButton_2 = QtWidgets.QPushButton(self.frame)
        self.pushButton_2.setGeometry(QtCore.QRect(300, 570, 541, 21))
        self.pushButton_2.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.pushButton_2.setStyleSheet("background-color: #F3F4F1;\n"
"color: rgb(0, 100, 142);\n"
"alternate-background-color: #F3F4F1;\n"
"border: 0px;\n"
"gridline-color: #F3F4F1;\n"
"selection-color: #F3F4F1;\n"
"selection-background-color: #F3F4F1;\n"
"font: 16px \"Segoe UI\";")
        self.pushButton_2.setObjectName("pushButton_2")
        self.listWidget = QtWidgets.QListWidget(self.frame)
        self.listWidget.setGeometry(QtCore.QRect(50, 100, 924, 450))
        self.listWidget.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.listWidget.setObjectName("listWidget")
        self.label = QtWidgets.QLabel(self.frame)
        self.label.setGeometry(QtCore.QRect(100, 60, 250, 30))
        font = QtGui.QFont()
        font.setPointSize(17)
        font.setBold(True)
        font.setWeight(75)
        self.label.setFont(font)
        self.label.setObjectName("label")
        self.horizontalLayout.addWidget(self.frame)
        spacerItem2 = QtWidgets.QSpacerItem(10, 600, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout.addItem(spacerItem2)
        self.verticalLayout.addLayout(self.horizontalLayout)
        spacerItem3 = QtWidgets.QSpacerItem(1041, 6, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout.addItem(spacerItem3)
        InitialRegSuccess.setCentralWidget(self.centralwidget)

        self.retranslateUi(InitialRegSuccess)
        QtCore.QMetaObject.connectSlotsByName(InitialRegSuccess)

    def retranslateUi(self, InitialRegSuccess):
        _translate = QtCore.QCoreApplication.translate
        InitialRegSuccess.setWindowTitle(_translate("InitialRegSuccess", "MainWindow"))
        self.PushButton_2.setWhatsThis(_translate("InitialRegSuccess", "<html><head/><body><p>fSf</p></body></html>"))
        self.pushButton_2.setText(_translate("InitialRegSuccess", "© 2019 Big Fat Designs, LLC. All rights Reserved. Learn More."))
        self.label.setText(_translate("InitialRegSuccess", "Choose a network: "))

import source_rc
