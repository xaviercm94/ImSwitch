# -*- coding: utf-8 -*-
"""
Created on Tue Mar 24 16:41:57 2020

@author: _Xavi
"""
import numpy as np

#class CameraHelper():
#    def __init__(self):
#    # Should the recorder be another helper?
#    def startAquisition(self):
#        
#    def stopAquisition(self):
#        
#    def changeParameter(self):
#        
#    def getLatestFrame(self):
#        
#    def getNewFrames(self):
        
class MasterController():
    
    def __init__(self):
        print('init master controller')
        self.stagePos = [0, 0, 0]

    def moveStage(self, axis, dist):
        self.stagePos[axis] += dist
        return self.stagePos[axis]
        
    def getImage(self):
        im = 20 + np.zeros((20, 20))
        return im
        
    def getImageSize(self):
        return [500, 500]
        
    def toggleLaser(self, enable, laser):
        print('Change enabler of laser '+ str(laser) + ' to ' + str(enable))
        
    def changePower(self, magnitude, laser):
        print('Change power of laser '+ str(laser) + ' to ' + str(magnitude))
        
    def digitalMod(self, digital, powers, laser):
        print('Digital modulation for laser '+ str(laser) + ' set to ' + str(digital))
        
