# -*- encoding:utf-8 -*-
import PyQt4
import sys
reload(sys)
import threading
from naoqi import ALProxy
from pygame.locals import *
from controlls.NaoSay import *
import pygame
from sys import exit
from PyQt4 import QtGui
from PyQt4 import QtCore
class NaoSpeakView(QtGui.QWidget):
    naoip=""
    naoport=9559
    def __init__(self,ip):
        super(NaoSpeakView,self).__init__()
        self.initUI()
        self.naoip=ip
        self.naosay = ALProxy("ALTextToSpeech",self.naoip,self.naoport)
        self.naosay.setLanguage("Chinese")
        sys.setdefaultencoding("utf-8")
    def initUI(self):
        self.btn = QtGui.QPushButton('Dialog', self)
        self.btn.move(20, 20)
        self.btn.clicked.connect(self.showDialog)

        self.le = QtGui.QLineEdit(self)
        self.le.move(130, 22)

        self.setGeometry(300, 300, 290, 150)
        self.setWindowTitle('Input dialog')
        self.show()
    def showDialog(self):
        text, ok = QtGui.QInputDialog.getText(self,'Input Dialog', 'What are you going to say:')
        if ok:
            self.naosay.say(str(text))



