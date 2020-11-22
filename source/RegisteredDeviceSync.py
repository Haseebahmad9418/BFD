# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'RegisteredDeviceSync.ui'
#
# Created by: PyQt5 UI code generator 5.9.2
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_DeviceSync(object):
    def setupUi(self, DeviceSync):
        DeviceSync.setObjectName("DeviceSync")
        DeviceSync.resize(1044, 620)
        DeviceSync.setStyleSheet("background-color: #F3F4F1;\n"
"QFrame\n"
"{\n"
"    background:#333;\n"
"}")
        self.centralwidget = QtWidgets.QWidget(DeviceSync)
        self.centralwidget.setObjectName("centralwidget")
        f=open("path.txt","r")
        d_path=f.read()
        f.close()
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
        self.label_6 = QtWidgets.QLabel(self.frame)
        self.label_6.setGeometry(QtCore.QRect(400, 60, 211, 101))
        self.label_6.setStyleSheet("image: url(:/newPrefix/logo_Big-Fat-Display.svg);")
        self.label_6.setText("")
        self.label_6.setPixmap(QtGui.QPixmap(d_path+"/source/Icons/logo_Big-Fat-Display.svg"))
        self.label_6.setScaledContents(True)
        self.label_6.setObjectName("label_6")
        self.PushButton_4 = QtWidgets.QPushButton(self.frame)
        self.PushButton_4.setGeometry(QtCore.QRect(407, 477, 261, 60))
        self.PushButton_4.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.PushButton_4.setStyleSheet("QPushButton{\n"
"font: 30px \"Segoe UI\";\n"
"background:#00648E;\n"
"color:white;\n"
"border-color: #00000066;\n"
"\n"
"border-radius:10px;\n"
"}")
        self.PushButton_4.setIconSize(QtCore.QSize(50, 53))
        self.PushButton_4.setObjectName("PushButton_4")
        self.PushButton_2 = QtWidgets.QPushButton(self.frame)
        self.PushButton_2.setGeometry(QtCore.QRect(360, 477, 61, 60))
        self.PushButton_2.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.PushButton_2.setStyleSheet("QPushButton{\n"
"background:#00648E;\n"
"color:white;\n"
"border-color: #00000066;\n"
"border:1px solid #00648E;\n"
"border-radius:10px;\n"
"}")
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("Icons/icon_sync.svg"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.PushButton_2.setIcon(icon)
        self.PushButton_2.setIconSize(QtCore.QSize(40, 50))
        self.PushButton_2.setObjectName("PushButton_2")
        self.label = QtWidgets.QLabel(self.frame)
        self.label.setGeometry(QtCore.QRect(184, 238, 331, 40))
        self.label.setStyleSheet("QLabel{\n"
"    font: 75 30px \"Segoe UI\";\n"
"color: #00648E;\n"
"size:30px;\n"
"\n"
"}")
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(self.frame)
        self.label_2.setGeometry(QtCore.QRect(184, 280, 677, 171))
        self.label_2.setStyleSheet("QLabel{\n"
"color: #00648E;\n"
"size:15px;\n"
"\n"
"}")
        self.label_2.setObjectName("label_2")
        self.label_3 = QtWidgets.QLabel(self.frame)
        self.label_3.setGeometry(QtCore.QRect(540, 275, 321, 181))
        self.label_3.setStyleSheet("QLabel{\n"
"color: #00648E;\n"
"size:15px;\n"
"\n"
"}")
        self.label_3.setObjectName("label_3")
        self.pushButton = QtWidgets.QPushButton(self.frame)
        self.pushButton.setGeometry(QtCore.QRect(290, 570, 511, 21))
        self.pushButton.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.pushButton.setStyleSheet("background-color: #F3F4F1;\n"
"color: rgb(0, 100, 142);\n"
"alternate-background-color: #F3F4F1;\n"
"border: 0px;\n"
"gridline-color: #F3F4F1;\n"
"selection-color: #F3F4F1;\n"
"selection-background-color: #F3F4F1;\n"
"font: 16px \"Segoe UI\";")
        self.pushButton.setObjectName("pushButton")
        self.horizontalLayout.addWidget(self.frame)
        spacerItem2 = QtWidgets.QSpacerItem(10, 600, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout.addItem(spacerItem2)
        self.verticalLayout.addLayout(self.horizontalLayout)
        spacerItem3 = QtWidgets.QSpacerItem(1041, 6, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout.addItem(spacerItem3)
        DeviceSync.setCentralWidget(self.centralwidget)

        self.retranslateUi(DeviceSync)
        QtCore.QMetaObject.connectSlotsByName(DeviceSync)

    def retranslateUi(self, DeviceSync):
        _translate = QtCore.QCoreApplication.translate
        DeviceSync.setWindowTitle(_translate("DeviceSync", "MainWindow"))
        self.PushButton_4.setWhatsThis(_translate("DeviceSync", "<html><head/><body><p>fSf</p></body></html>"))
        self.PushButton_4.setText(_translate("DeviceSync", "Retry Download"))
        self.PushButton_2.setWhatsThis(_translate("DeviceSync", "<html><head/><body><p>fSf</p></body></html>"))
        self.label.setText(_translate("DeviceSync", "<html><head/><body><p><span style=\" font-size:30px; font-weight:600;\">Synching Content</span></p></body></html>"))
        self.label_2.setText(_translate("DeviceSync", "<html><head/><body><p><span style=\" font-size:30px; color:#00648e;\">Contacting Server</span></p><p><span style=\" font-size:30px; color:#00648e;\">Checking Files</span></p><p><span style=\" font-size:30px; color:#00648e;\">Downloading Content</span></p><p><span style=\" font-size:30px; color:#b10023;\">File Transfer Interrupted</span></p></body></html>"))
        self.label_3.setText(_translate("DeviceSync", "<html><head/><body><p align=\"right\"><span style=\" font-size:30px; color:#00648e;\">.................. Success!</span></p><p align=\"right\"><span style=\" font-size:30px; color:#00648e;\">.................. Success!</span></p><p align=\"right\"><span style=\" font-size:30px; color:#00648e;\">..................... </span><span style=\" font-size:30px; color:#b10023;\">ERROR</span></p><p align=\"right\"><br/></p></body></html>"))
        self.pushButton.setText(_translate("DeviceSync", "© 2019 Big Fat Designs, LLC. All rights Reserved. Learn More."))

import source_rc
