'''
Created on Sep 13, 2017

@author: ddimarcello
'''
import sys
from scripts.main_gui import *
from scripts.globals import *

class Launcher:
    
    def __init__(self):
        
        def Play():
            Globals.scene = "game"

        def Exit():
            sys.exit()
        
        window_width = 800
        
        btnPlay = Menu.Button(text = "Play", rect = (0,0, 300, 60), tag = ("menu", None))
        btnPlay.Left = window_width / 2 - btnPlay.Width / 2
        btnPlay.Top = 100
        btnPlay.Command = Play
        
        btnSave = Menu.Button(text = "Save", rect = (0, 0, 300, 60), tag = ("menu", None))
        btnSave.Left = window_width / 2 - btnPlay.Width / 2
        btnSave.Left = btnPlay.Left
        btnSave.Top = btnPlay.Top + btnSave.Height + 3
        
        btnLoad = Menu.Button(text = "Load", rect = (0, 0, 300, 60), tag = ("menu", None))
        btnLoad.Left = window_width / 2 - btnPlay.Width / 2
        btnLoad.Left = btnPlay.Left
        btnLoad.Top = btnPlay.Top + (btnLoad.Height + 3)*2
        
        btnExit = Menu.Button(text = "Exit", rect = (0, 0, 300, 60), tag = ("menu", None))
        btnExit.Left = window_width / 2 - btnPlay.Width / 2
        btnExit.Left = btnPlay.Left
        btnExit.Top = btnPlay.Top + (btnExit.Height + 3)*3
        btnExit.Command = Exit

    
    