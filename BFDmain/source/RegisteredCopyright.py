# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'RegisteredCopyright.ui'
#
# Created by: PyQt5 UI code generator 5.9.2
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_RegisteredCopyright(object):
    def setupUi(self, RegisteredCopyright):
        RegisteredCopyright.setObjectName("RegisteredCopyright")
        RegisteredCopyright.resize(1044, 620)
        RegisteredCopyright.setStyleSheet("background-color: #F3F4F1;\n"
"QFrame\n"
"{\n"
"    background:#333;\n"
"}")
        self.centralwidget = QtWidgets.QWidget(RegisteredCopyright)
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
        self.frame.setMaximumSize(QtCore.QSize(1024, 600))
        self.frame.setMouseTracking(True)
        self.frame.setStyleSheet("QFrame{\n"
"background:#F3F4F1\n"
"}\n"
"")
        self.frame.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame.setObjectName("frame")
        self.label = QtWidgets.QLabel(self.frame)
        self.label.setGeometry(QtCore.QRect(730, 474, 156, 86))
        self.label.setStyleSheet("image: url(:/newPrefix/powered-by-raspberry-pi-vector-logo.svg);")
        self.label.setText("")
        self.label.setPixmap(QtGui.QPixmap(d_path+"/source/Icons/raspberrypi.png"))
        self.label.setScaledContents(True)
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(self.frame)
        self.label_2.setGeometry(QtCore.QRect(368, 35, 248, 135))
        self.label_2.setMinimumSize(QtCore.QSize(248, 135))
        self.label_2.setMaximumSize(QtCore.QSize(248, 135))
        self.label_2.setSizeIncrement(QtCore.QSize(248, 135))
        self.label_2.setStyleSheet("image: url(:/newPrefix/logo_Big-Fat-Designs.svg);")
        self.label_2.setText("")
        self.label_2.setPixmap(QtGui.QPixmap(d_path+"/source/Icons/logo_Big-Fat-Display.svg"))
        self.label_2.setScaledContents(True)
        self.label_2.setObjectName("label_2")
        self.label_11 = QtWidgets.QLabel(self.frame)
        self.label_11.setGeometry(QtCore.QRect(322, 188, 421, 40))
        self.label_11.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.label_11.setStyleSheet("font: 75 11pt \"Segoe UI\";")
        self.label_11.setObjectName("label_11")
        self.label_12 = QtWidgets.QLabel(self.frame)
        self.label_12.setGeometry(QtCore.QRect(130, 245, 764, 101))
        self.label_12.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.label_12.setStyleSheet("QLabel{\n"
"    font: 16px \"Segoe UI\";\n"
"color: #00648E;\n"
"size:16px;\n"
"top:300;\n"
"\n"
"}")
        self.label_12.setObjectName("label_12")
        self.label_13 = QtWidgets.QLabel(self.frame)
        self.label_13.setGeometry(QtCore.QRect(260, 350, 291, 91))
        self.label_13.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.label_13.setStyleSheet("QLabel{\n"
"    font: 30px \"Segoe UI\";\n"
"color: #00648E;\n"
"size:30px;\n"
"top:300;\n"
"\n"
"}")
        self.label_13.setObjectName("label_13")
        self.pushButton_2 = QtWidgets.QPushButton(self.frame)
        self.pushButton_2.setGeometry(QtCore.QRect(181, 490, 136, 70))
        self.pushButton_2.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.pushButton_2.setStyleSheet("QPushButton{\n"
"background:#F3F4F1;\n"
"color:#F3F4F1;\n"
"border-color: #F3F4F1;\n"
"border:1px solid #F3F4F1;\n"
"border-radius:10px;\n"
"}\n"
"")
        self.pushButton_2.setText("")
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("Icons/logo_Big-Fat-Display.svg"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.pushButton_2.setIcon(icon)
        self.pushButton_2.setIconSize(QtCore.QSize(130, 100))
        self.pushButton_2.setObjectName("pushButton_2")
        self.label_3 = QtWidgets.QLabel(self.frame)
        self.label_3.setGeometry(QtCore.QRect(540, 350, 150, 31))
        self.label_3.setStyleSheet("\n"
"    font: 30px \"Segoe UI\";\n"
"color: #00648E;\n"
"size:30px;\n"
"top:300;\n"
"\n"
"")
        self.label_3.setText("")
        self.label_3.setObjectName("label_3")
        self.label_4 = QtWidgets.QLabel(self.frame)
        self.label_4.setGeometry(QtCore.QRect(540, 400, 150, 41))
        self.label_4.setStyleSheet("font: 30px \"Segoe UI\";\n"
"color: #00648E;\n"
"size:30px;\n"
"top:300;")
        self.label_4.setText("")
        self.label_4.setObjectName("label_4")
        self.horizontalLayout.addWidget(self.frame)
        spacerItem2 = QtWidgets.QSpacerItem(10, 600, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout.addItem(spacerItem2)
        self.verticalLayout.addLayout(self.horizontalLayout)
        spacerItem3 = QtWidgets.QSpacerItem(1041, 6, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout.addItem(spacerItem3)
        RegisteredCopyright.setCentralWidget(self.centralwidget)

        self.retranslateUi(RegisteredCopyright)
        QtCore.QMetaObject.connectSlotsByName(RegisteredCopyright)

    def retranslateUi(self, RegisteredCopyright):
        _translate = QtCore.QCoreApplication.translate
        RegisteredCopyright.setWindowTitle(_translate("RegisteredCopyright", "MainWindow"))
        self.label_11.setText(_translate("RegisteredCopyright", "<html><head/><body><p><span style=\" font-size:30px; font-weight:600; color:#141f35;\">http://bigfatdesigns.com</span></p></body></html>"))
        self.label_12.setText(_translate("RegisteredCopyright", "<html><head/><body><p align=\"center\">Big Fat Display is owned and disributed by Big Fat Designs, LLC.</p><p align=\"center\">For more information about Big Fat Display or if you need assistance,please contact us through our website.</p><p align=\"center\">© 2019 Big Fat Designs, LLC. All rights Reserved. </p></body></html>"))
        self.label_13.setText(_translate("RegisteredCopyright", "<html><head/><body><p align=\"center\">Customer ID</p><p align=\"center\">Software ID</p></body></html>"))

import source_rc
