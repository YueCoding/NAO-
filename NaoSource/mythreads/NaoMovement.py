# -*- encoding:UTF-8 -*-
import threading
from views.test import *
from naoqi import ALProxy
import pygame
import time
from pygame.locals import *
from sys import exit
from PyQt4 import QtGui
class NaoMovement(threading.Thread):
    IP = ""
    PORT = 9559
    def __init__(self,IPNAO):
        threading.Thread.__init__(self)
        self.IP = IPNAO
    def getIP(self, NMIP):
        return self.IP
    def run(self):
        nNaoMove=ALProxy("ALMotion", self.IP, self.PORT)
        postureProxy = ALProxy("ALRobotPosture", self.IP, self.PORT)
        nNaoMove.wakeUp()
        postureProxy.goToPosture("Stand", 0.5)
        pygame.init()
        screen = pygame.display.set_mode((454, 603), 0, 32)
        background = pygame.image.load(r"F:\NaoTest\NaoSource\mythreads\naonew.png").convert_alpha()
        pygame.display.set_caption("Dragon's dance")
        screen.blit(background, (0, 0))
        pygame.display.update()
        while True:
            for event in pygame.event.get():
                if event.type == QUIT:
                    exit()
                elif event.type == KEYDOWN:
                    if event.key == K_UP:
                        x = 0.7
                        y = 0.0
                        theta = 0.0
                        frequency = 0.4
                        nNaoMove.moveToward(x, y, theta, [["Frequency", frequency]])

                    elif event.key == K_DOWN:
                        x = -0.4
                        y = 0.0
                        theta = 0.0
                        frequency = 0.2
                        nNaoMove.moveToward(x, y, theta, [["Frequency", frequency]])
                    elif event.key == K_LEFT:
                        x = 0.0
                        y = 0.2
                        theta = 0.6
                        frequency = 0.4
                        nNaoMove.moveToward(x, y, theta, [["Frequency", frequency]])
                    elif event.key == K_RIGHT:
                        x = 0.0
                        y = -0.2
                        theta = -0.6
                        frequency = 0.4
                        nNaoMove.moveToward(x, y, theta, [["Frequency", frequency]])
                    elif event.key == K_q:
                        nNaoMove.stopMove()
                        time.sleep(1)
                        nNaoMove.rest()
                    elif event.key == K_r:
                        nNaoMove.wakeUp()
                        postureProxy.goToPosture("StandInit", 0.5)
                        time.sleep(1.5)
                    elif event.key == K_s:
                        nNaoMove.stopMove()

                    elif event.key == K_z:
                        # 头部左转
                        nNaoMove.setStiffnesses("Head", 1.0)
                        names = "HeadYaw"
                        changes = 0.5
                        fractionMaxSpeed = 0.1
                        nNaoMove.changeAngles(names, changes, fractionMaxSpeed)
                    elif event.key == K_c:
                        # 头部右转
                        nNaoMove.setStiffnesses("Head", 1)
                        names = "HeadYaw"
                        changes = -0.5
                        fractionMaxSpeed = 0.1
                        nNaoMove.changeAngles(names, changes, fractionMaxSpeed)
                    elif event.key == K_a:
                        # 向上看
                        nNaoMove.setStiffnesses("Head", 1)
                        names = "HeadPitch"
                        changes = 0.2
                        fractionMaxSpeed = 0.1
                        nNaoMove.changeAngles(names, changes, fractionMaxSpeed)
                    elif event.key == K_d:
                        # 向下看
                        nNaoMove.setStiffnesses("Head", 1)
                        names = "HeadPitch"
                        changes = -0.2
                        fractionMaxSpeed = 0.1
                        nNaoMove.changeAngles(names, changes, fractionMaxSpeed)
                    elif event.key == K_x:
                        # 头部恢复
                        nNaoMove.setStiffnesses("Head", 1)
                        names = "HeadYaw"
                        angles = 0.0
                        fractionMaxSpeed = 0.2
                        nNaoMove.setAngles(names, angles, fractionMaxSpeed)
                        # 左手运动
                    elif event.key == K_1:
                        changes = -0.25
                        fractionMaxSpeed = 0.1
                        nNaoMove.setStiffnesses("LShoulderPitch", 1)
                        nNaoMove.changeAngles("LShoulderPitch", changes, 0.1)  # (关节，改变的角度，快慢）
                    elif event.key == K_2:
                        changes = 0.25
                        nNaoMove.changeAngles("LShoulderPitch", changes, 0.1)
                    elif event.key == K_3:
                        changes = 0.2
                        nNaoMove.setStiffnesses("LShoulderRoll", 1)
                        nNaoMove.changeAngles("LShoulderRoll", changes, 0.1)
                    elif event.key == K_4:
                        changes = -0.2
                        nNaoMove.changeAngles("LShoulderRoll", changes, 0.1)
                    elif event.key == K_6:
                        changes = 0.3
                        nNaoMove.setStiffnesses("LElbowRoll", 1)
                        nNaoMove.changeAngles("LElbowRoll", changes, 0.1)
                    elif event.key == K_5:
                        changes = -0.3
                        nNaoMove.changeAngles("LElbowRoll", changes, 0.1)
                    elif event.key == K_7:
                        nNaoMove.post.openHand("LHand")
                    elif event.key == K_8:
                        nNaoMove.post.closeHand("LHand")
                        # 右手运动
                    elif event.key == K_y:
                        names = "RShoulderPitch"
                        changes = -0.25
                        nNaoMove.setStiffnesses(names, 1)
                        nNaoMove.changeAngles(names, changes, 0.1)
                    elif event.key == K_u:
                        names = "RShoulderPitch"
                        changes = 0.25
                        nNaoMove.changeAngles(names, changes, 0.1)
                    elif event.key == K_i:
                        names = "RShoulderRoll"
                        changes = -0.2
                        nNaoMove.setStiffnesses(names, 1)
                        nNaoMove.changeAngles(names, changes, 0.1)
                    elif event.key == K_o:
                        names = "RShoulderRoll"
                        changes = 0.2
                        nNaoMove.changeAngles(names, changes, 0.1)
                    elif event.key == K_h:
                        names = "RElbowRoll"
                        changes = 0.3
                        nNaoMove.setStiffnesses(names, 1)
                        nNaoMove.changeAngles(names, changes, 0.1)
                    elif event.key == K_j:
                        names = "RElbowRoll"
                        changes = -0.3
                        nNaoMove.changeAngles(names, changes, 0.1)
                    elif event.key == K_k:
                        names = "RHand"
                        nNaoMove.post.openHand(names)
                    elif event.key == K_l:
                        names = "RHand"
                        nNaoMove.post.closeHand(names)
