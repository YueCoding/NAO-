# -*- encoding:utf-8 -*-
import threading
from naoqi import ALProxy
import time

class shuo(threading.Thread):
    IP = ""
    def __init__(self, robotIP):
        self.IP = robotIP
        threading.Thread.__init__(self)
        self.audio = ALProxy("ALTextToSpeech", self.IP, 9559)

    def run(self):
        self.audio.setLanguage("Chinese")
        self.audio.say("嘿，我身上没有病毒！")
        time.sleep(0.5)
        self.audio.say("我可以进去，哈！")