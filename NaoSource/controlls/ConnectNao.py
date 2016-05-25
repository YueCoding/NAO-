# -*- encoding: utf-8 -*-
class ConnectNao:
    NaoIP=""
    def __init__(self):
        self.NaoPort = 9559
    def setNaoIP(self,InNaoIP):
        self.NaoIP = InNaoIP
    def getNaoIP(self):
        return self.NaoIP
    def getNaoPort(self):
        return self.NaoPort


