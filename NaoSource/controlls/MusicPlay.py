# -*- encoding:utf-8 -*-
import threading
from naoqi import ALProxy

class MusicPlay(threading.Thread):
    NAOIP = ""
    def __init__(self,IP):
        self.NAOIP = IP
        threading.Thread.__init__(self)
        self.nplaymusic = ALProxy("ALAudioPlayer", self.NAOIP, 9559)
    def run(self):
        File = self.nplaymusic.loadFile("/home/nao/naoqi/music.mp3")
        self.nplaymusic.play(File)
