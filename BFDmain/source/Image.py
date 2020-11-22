from PyQt5 import QtCore, QtGui, QtWidgets
# from Tesstt import Ui_OsamaWindow

from PyQt5.QtMultimediaWidgets import QVideoWidget
from PyQt5 import QtMultimedia

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(1024, 631)
        MainWindow.setWindowFlags(QtCore.Qt.CustomizeWindowHint)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.photo_label = QtWidgets.QLabel(self.centralwidget)
        self.photo_label.setGeometry(QtCore.QRect(400, 0, 1024, 631))
        self.photo_label.setText("")
        self.photo_label.setObjectName("photo_label")


        # self.photo_label.doubleClickEvent.connect(self.double_clickked_function)
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)
        

    # def double_clickked_function(self):
    #     self.window = QtWidgets.QMainWindow()
    #     self.ui = Ui_OsamaWindow()
    #     self.ui.setupUi(self.window)
    #     self.window.show()
    #     Ui_MainWindow.hide()
    
##
##        self.Video_Widget = QVideoWidget(self.centralwidget)
##        self.Video_Widget.setGeometry(QtCore.QRect(0, 0, 711, 361))
##        self.Video_Widget.setObjectName("Video_Widget")
##        self.play = QtWidgets.QPushButton(self.centralwidget)
##        self.play.setGeometry(QtCore.QRect(10, 410, 75, 23))
##        self.play.setObjectName("play")
##        self.enable = QtWidgets.QPushButton(self.centralwidget)
##        self.enable.setGeometry(QtCore.QRect(100, 410, 75, 23))
##        self.enable.setObjectName("enable")
##        self.fullscreen = QtWidgets.QPushButton(self.centralwidget)
##        self.fullscreen.setGeometry(QtCore.QRect(190, 410, 75, 23))
##        self.fullscreen.setObjectName("fullscreen")
##
##        MainWindow.setCentralWidget(self.centralwidget)
##
##        self.retranslateUi(MainWindow)
##        QtCore.QMetaObject.connectSlotsByName(MainWindow)
##        
##        self.player = QtMultimedia.QMediaPlayer()
##        self.player.setVideoOutput(self.Video_Widget)
##        PATH1 = "/home/abbad/Desktop/Osama/Actual_data/DJVHHUAY.mp4"
##        self.player.setMedia(QtMultimedia.QMediaContent(QtCore.QUrl.fromLocalFile(PATH1)))
##        PATH2 = "/home/abbad/Desktop/Osama/Actual_data/J9BLA3EC.mp4"
##        self.enable.clicked.connect(self.enableFunc)
##        self.fullscreen.clicked.connect(self.fullscreenFunc)
##        self.play.clicked.connect(self.player.play)
##        self.play.setText( "Play")
##        self.enable.setText("Change")
##        self.fullscreen.setText("Fullscreen")
##        
##

##
##    def enableFunc(self, MainWindow):
##        PATH2 = "/home/abbad/Desktop/Osama/Actual_data/J9BLA3EC.mp4"
##        self.player.setMedia(QtMultimedia.QMediaContent(QtCore.QUrl.fromLocalFile(PATH2)))
##        self.player.play()
##
##    def fullscreenFunc(self, MainWindow):
##        self.Video_Widget.setFullScreen(True)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
