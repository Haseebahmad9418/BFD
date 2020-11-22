# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'Main.ui'
#
# Created by: PyQt5 UI code generator 5.9.2
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_Main(object):
    def setupUi(self, Main):
        Main.setObjectName("Main")
        Main.resize(1056, 620)
        Main.setStyleSheet("background-color: #F3F4F1;\n"
"QFrame\n"
"{\n"
"    background:#333;\n"
"}")
        self.centralwidget = QtWidgets.QWidget(Main)
        self.centralwidget.setObjectName("centralwidget")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.centralwidget)
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout.setSpacing(0)
        self.verticalLayout.setObjectName("verticalLayout")
        spacerItem = QtWidgets.QSpacerItem(1044, 6, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
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
        self.frame.setFrameShadow(QtWidgets.QFrame.Plain)
        self.frame.setObjectName("frame")
        self.PushButton = QtWidgets.QPushButton(self.frame)
        self.PushButton.setGeometry(QtCore.QRect(163, 251, 316, 204))
        self.PushButton.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.PushButton.setStyleSheet("QPushButton{\n"
"    font: 30px \"Segoe UI\";\n"
"background:#000000;\n"
"color:white;\n"
"border-color: #00000066;\n"
"border:1px solid #00648E;\n"
"border-radius:10px;\n"
"}")
        self.PushButton.setObjectName("PushButton")
        self.label_3 = QtWidgets.QLabel(self.frame)
        self.label_3.setGeometry(QtCore.QRect(100, 172, 831, 41))
        self.label_3.setStyleSheet("QLabel{\n"
"font: 75 11pt \"Segoe UI\";\n"
"color: #00648E;\n"
"size:30px;\n"
"\n"
"}")
        self.label_3.setObjectName("label_3")
        f=open("path.txt","r")
        d_path=f.read()
        f.close()
        self.label_6 = QtWidgets.QLabel(self.frame)
        self.label_6.setGeometry(QtCore.QRect(407, 30, 210, 108))
        self.label_6.setStyleSheet("image: url(:/newPrefix/logo_Big-Fat-Display.svg);")
        self.label_6.setText("")
        self.label_6.setPixmap(QtGui.QPixmap(d_path+"/source/Icons/logo_Big-Fat-Display.svg"))
        self.label_6.setScaledContents(True)
        self.label_6.setObjectName("label_6")
        self.PushButton_2 = QtWidgets.QPushButton(self.frame)
        self.PushButton_2.setGeometry(QtCore.QRect(545, 251, 316, 204))
        self.PushButton_2.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.PushButton_2.setStyleSheet("QPushButton{\n"
"background:#000000;\n"
"    font: 30px \"Segoe UI\";\n"
"color:white;\n"
"border-color: #00000066;\n"
"border:1px solid #00648E;\n"
"border-radius:10px;\n"
"}")
        self.PushButton_2.setObjectName("PushButton_2")
        self.label = QtWidgets.QLabel(self.frame)
        self.label.setGeometry(QtCore.QRect(476, 498, 96, 52))
        self.label.setStyleSheet("image: url(:/newPrefix/logo_Big-Fat-Designs.svg);")
        self.label.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.label.setText("")
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(self.frame)
        self.label_2.setGeometry(QtCore.QRect(342, 568, 411, 31))
        self.label_2.setStyleSheet("color: rgb(0, 100, 142);\n"
"font: 16px \"Segoe UI\";")
        self.label_2.setObjectName("label_2")
        self.horizontalLayout.addWidget(self.frame)
        spacerItem2 = QtWidgets.QSpacerItem(10, 600, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout.addItem(spacerItem2)
        self.verticalLayout.addLayout(self.horizontalLayout)
        spacerItem3 = QtWidgets.QSpacerItem(1044, 6, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout.addItem(spacerItem3)
        Main.setCentralWidget(self.centralwidget)

        self.retranslateUi(Main)
        QtCore.QMetaObject.connectSlotsByName(Main)

    def retranslateUi(self, Main):
        _translate = QtCore.QCoreApplication.translate
        Main.setWindowTitle(_translate("Main", "MainWindow"))
        self.PushButton.setWhatsThis(_translate("Main", "<html><head/><body><p>fSf</p></body></html>"))
        self.PushButton.setText(_translate("Main", "First Time Install\n"
"    --\n"
"Register New Device"))
        self.label_3.setText(_translate("Main", "<html><head/><body><p><span style=\" font-size:30px; font-weight:600; color:#00648e;\">For Developers: Select The Workflow To Preview</span></p></body></html>"))
        self.PushButton_2.setWhatsThis(_translate("Main", "<html><head/><body><p>fSf</p></body></html>"))
        self.PushButton_2.setText(_translate("Main", "Standard Bootup\n"
"    --\n"
"Registered Device"))
        self.label_2.setWhatsThis(_translate("Main", "© 2019 Big Fat Designs, LLC All rights Reserved."))
        self.label_2.setText(_translate("Main", "<html><head/><body><p align=\"center\"><span style=\" font-size:16px; color:#00648e;\">© 2019 Big Fat Designs, LLC All rights Reserved.</span></p></body></html>"))

