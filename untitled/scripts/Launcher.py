'''
Created on Sep 13, 2017

@author: ddimarcello
'''
import sys

from scripts.globals import *
from scripts.main_gui import *


class Launcher:
    
    def __init__(self):
        
        def Play():
            Globals.main_scene = "game"

        def Exit():
            sys.exit()
        
        window_width = 800
        
        btnPlay = Menu.Button(text = "Play", rect = (0,0, 300, 60), bg  = Color.Gray, fg = Color.White, bgr = Color.CornflowerBlue, tag = ("menu", None))
        btnPlay.Left = window_width / 2 - btnPlay.Width / 2
        btnPlay.Top = 100
        btnPlay.Command = Play
        
        btnSave = Menu.Button(text = "Save", rect = (0, 0, 300, 60), bg  = Color.Gray, fg = Color.White, bgr = Color.CornflowerBlue, tag = ("menu", None))
        btnSave.Left = btnPlay.Left
        btnSave.Top = btnPlay.Top + btnSave.Height + 3
        
        btnLoad = Menu.Button(text = "Load", rect = (0, 0, 300, 60), bg  = Color.Gray, fg = Color.White, bgr = Color.CornflowerBlue, tag = ("menu", None))
        btnLoad.Left = btnPlay.Left
        btnLoad.Top = btnPlay.Top + (btnLoad.Height + 3)*2
        
        btnExit = Menu.Button(text = "Exit", rect = (0, 0, 300, 60), bg  = Color.Gray, fg = Color.White, bgr = Color.CornflowerBlue, tag = ("menu", None))
        btnExit.Left = btnPlay.Left
        btnExit.Top = btnPlay.Top + (btnExit.Height + 3)*3
        btnExit.Command = Exit

    
    