import requests
import json
import os,sys
from os import path
import urllib
import download
from PyQt5.QtCore import QTimer
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtCore import pyqtSignal
from wifi import Ui_Wifilist
from wifipassword import Ui_Wifi
from subprocess import check_output


class wifilisting(QtWidgets.QMainWindow, Ui_Wifilist):  #Class to acces Main.py GUI
    refresh = pyqtSignal()

    def __init__(self):
        QtWidgets.QWidget.__init__(self)
        super(Ui_Wifilist, self).__init__()
        self.setupUi(self)
        self.PushButton_2.clicked.connect(lambda: self.refreshlist())
        self.refreshlist()
        self.listWidget.clicked.connect(self.clicked)

    def clicked(self,item):
        global selectedssid
        item=self.listWidget.currentItem()
        selectedssid=item.text()
        print(item.text())
        self.refresh.emit()
        pass

    def refreshlist(self):
       scanoutput = check_output(["iwlist", "wlan0", "scan"])
       ss=scanoutput.decode("utf-8")
       self.listWidget.clear()
       ssid=[]
       for line in ss.split("\n"):
           if "ESSID" in line:
               ssid = line.split('"')[1]
               print(ssid)
               item=QtWidgets.QListWidgetItem(ssid,self.listWidget)
               item.setTextAlignment(QtCore.Qt.AlignCenter)
               #self.ssidlist.addItem(item)
        
class wifipw(QtWidgets.QMainWindow, Ui_Wifi):  #Class to acces Main.py GUI
    switch_wpdone = QtCore.pyqtSignal()

    def __init__(self):
        QtWidgets.QWidget.__init__(self)
        super(Ui_Wifi, self).__init__()
        self.setupUi(self)
        self.PushButton_2.clicked.connect(lambda: self.connectwifi())

        
    def connectwifi(self):
        global selectedssid
        print(selectedssid)
        pw=self.lineEdit.text()
        print(pw)
        wififile=debugmode.dpath+"pidata/wifi.txt"
        wfile=os.path.isfile(wififile)
        if(wfile==False):
            file1=open(wififile,'w+')
            file1.write("")
            file1.close()
        file1=open(wififile,'w+')
        data=selectedssid+"; "+pw+"; "
        file1.write(data)
        file1.close()
        self.switch_wpdone.emit()
        pass
class Controller:   # Controller class which controlls all the functions
    def __init__(self):
        print("In controller class")
        self._wifilisting=wifilisting()
        self._wifipw=wifipw()
        pass
    def conectivity(self):
        try:
            urllib.request.urlopen("https://www.google.com/",timeout=2)
            return True
        except:
            return False
    
    def show_wifilisting_page(self):
        self._wifilisting.close()
        self._wifilisting=wifilisting()
        self._wifilisting.refresh.connect(self.show_wifipw_page)
        self._wifilisting.showFullScreen()
        
    def show_wifipw_page(self):
        self._wifipw.close()
        self._wifipw=wifipw()
        self._wifipw.switch_wpdone.connect(show_Launch_page())
        self._wifipw.showFullScreen()
    def show_Launch_page(self):
        pass
    
if __name__ == "__main__":
    print("Main")
    app = QtWidgets.QApplication(sys.argv)
    controller = Controller()
    print("Calling splash")
    file = open("path.txt", "r")
    directoryPath = file.read()
    e = path.exists(directoryPath+"/source/credentials.txt")
    print(e)
    internet=controller.conectivity()
    if internet== True:
        controller.show_wifilisting_page()
    sys.exit(app.exec_())