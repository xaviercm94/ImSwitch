# -*- coding: utf-8 -*-
"""
Created on Fri Mar 20 15:13:24 2020

@author: _Xavi
"""
from pyqtgraph.Qt import QtGui
import view.widgets as widgets
import sys
from pyqtgraph.console import ConsoleWidget
import pyqtgraph as pg
import numpy as np
import os
import view.guitools as guitools

class TempestaView():
    
    def __init__(self, model):

        self.model = model
        self.app = QtGui.QApplication([])
        self.win = QtGui.QMainWindow()    

    def setController(self, controller):
        self.controller = controller
        
    def startView(self):
        # Shortcuts
        # TODO
        
        # Menu Bar
        # TODO

        
        self.win.setWindowTitle('Tempesta 2.0')
        self.win.cwidget = QtGui.QWidget()
        self.win.setCentralWidget(self.win.cwidget)

        layout = QtGui.QGridLayout()
        self.win.cwidget.setLayout(layout)
        
        # Presets
        self.presetsMenu = QtGui.QComboBox()
        self.controlFolder = os.path.split(os.path.realpath(__file__))[0]
        os.chdir(self.controlFolder)
        self.presetDir = os.path.join(self.controlFolder, 'presets')

        if not os.path.exists(self.presetDir):
            os.makedirs(self.presetDir)

        for preset in os.listdir(self.presetDir):
            self.presetsMenu.addItem(preset)
        self.loadPresetButton = QtGui.QPushButton('Load preset')

        #def loadPresetFunction(): return guitools.loadPreset(self)
        #self.loadPresetButton.pressed.connect(loadPresetFunction)

        layout.addWidget(self.presetsMenu, 0, 0)
        layout.addWidget(self.loadPresetButton, 0, 1)
        
        # Add all other Widgets
        self.settingsWidget = widgets.SettingsWidget()
        layout.addWidget(self.settingsWidget, 1, 0, 2, 2)
        
        self.imageWidget = widgets.ImageWidget()
        layout.addWidget(self.imageWidget, 0, 2, 6, 1)
        
        self.viewCtrlWidget = widgets.ViewCtrlWidget(self.imageWidget.vb)
        layout.addWidget(self.viewCtrlWidget, 3, 0, 1, 2)
        
        self.recordingWidget = widgets.RecordingWidget()
        layout.addWidget(self.recordingWidget, 4, 0, 1, 2)
        
        console = ConsoleWidget(namespace={'pg': pg, 'np': np})
        layout.addWidget(console, 5, 0, 1, 2)
        # TODO
        layout.setRowMinimumHeight(2, 175)
        layout.setRowMinimumHeight(3, 100)
        layout.setRowMinimumHeight(5, 175)
        layout.setColumnMinimumWidth(0, 275)
        layout.setColumnMinimumWidth(2, 1350)
        self.imageWidget.ci.layout.setColumnFixedWidth(1, 1150)
        self.imageWidget.ci.layout.setRowFixedHeight(1, 1150)
        
        self.win.show()
        sys.exit(self.app.exec_())
        
