# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'RegistedDeviceDownloadingcontent.ui'
#
# Created by: PyQt5 UI code generator 5.9.2
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_SyncSuccess(object):
    def setupUi(self, SyncSuccess):
        SyncSuccess.setObjectName("SyncSuccess")
        SyncSuccess.resize(1044, 620)
        SyncSuccess.setStyleSheet("background-color: #F3F4F1;\n"
"QFrame\n"
"{\n"
"    background:#333;\n"
"}")
        self.centralwidget = QtWidgets.QWidget(SyncSuccess)
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
        f=open("path.txt","r")
        d_path=f.read()
        f.close()
        self.label_6 = QtWidgets.QLabel(self.frame)
        self.label_6.setGeometry(QtCore.QRect(400, 60, 211, 101))
        self.label_6.setStyleSheet("image: url(:/newPrefix/logo_Big-Fat-Display.svg);")
        self.label_6.setText("")
        self.label_6.setPixmap(QtGui.QPixmap(d_path+"/source/Icons/logo_Big-Fat-Display.svg"))
        self.label_6.setScaledContents(True)
        self.label_6.setObjectName("label_6")
        self.label = QtWidgets.QLabel(self.frame)
        self.label.setGeometry(QtCore.QRect(184, 238, 311, 40))
        self.label.setStyleSheet("QLabel{\n"
"    font: 75 30px \"Segoe UI\";\n"
"color: #00648E;\n"
"size:30px;\n"
"\n"
"}")
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(self.frame)
        self.label_2.setGeometry(QtCore.QRect(184, 280, 677, 131))
        self.label_2.setStyleSheet("QLabel{\n"
"color: #00648E;\n"
"size:15px;\n"
"\n"
"}")
        self.label_2.setObjectName("label_2")
        self.label_3 = QtWidgets.QLabel(self.frame)
        self.label_3.setGeometry(QtCore.QRect(510, 285, 351, 131))
        self.label_3.setStyleSheet("QLabel{\n"
"color: #00648E;\n"
"size:15px;\n"
"\n"
"}")
        self.label_3.setObjectName("label_3")
        self.pushButton_2 = QtWidgets.QPushButton(self.frame)
        self.pushButton_2.setGeometry(QtCore.QRect(270, 570, 511, 21))
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
        self.horizontalLayout.addWidget(self.frame)
        spacerItem2 = QtWidgets.QSpacerItem(10, 600, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout.addItem(spacerItem2)
        self.verticalLayout.addLayout(self.horizontalLayout)
        spacerItem3 = QtWidgets.QSpacerItem(1041, 6, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout.addItem(spacerItem3)
        SyncSuccess.setCentralWidget(self.centralwidget)

        self.retranslateUi(SyncSuccess)
        QtCore.QMetaObject.connectSlotsByName(SyncSuccess)

    def retranslateUi(self, SyncSuccess):
        _translate = QtCore.QCoreApplication.translate
        SyncSuccess.setWindowTitle(_translate("SyncSuccess", "MainWindow"))
        self.label.setText(_translate("SyncSuccess", "<html><head/><body><p><span style=\" font-size:30px; font-weight:600;\">Synching Content</span></p></body></html>"))
        self.label_2.setText(_translate("SyncSuccess", "<html><head/><body><p><span style=\" font-size:30px; color:#00648e;\">Contacting Server</span></p><p><span style=\" font-size:30px; color:#00648e;\">Checking Files</span></p><p><span style=\" font-size:30px; color:#00648e;\">Downloading Content</span></p></body></html>"))
        self.label_3.setText(_translate("SyncSuccess", "<html><head/><body><p align=\"right\"><span style=\" font-size:30px; color:#00648e;\">.................. Success!</span></p><p align=\"right\"><span style=\" font-size:30px; color:#00648e;\">.................. Success!</span></p><p align=\"right\"><span style=\" font-size:30px; color:#00648e;\">..................................</span></p></body></html>"))
        self.pushButton_2.setText(_translate("SyncSuccess", "© 2019 Big Fat Designs, LLC. All rights Reserved. Learn More."))

import source_rc
