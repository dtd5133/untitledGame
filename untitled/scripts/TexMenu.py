'''
Created on Sep 14, 2017

@author: ddimarcello
'''
import pygame
from scripts.UltraColor import Color
from scripts.globals import Globals
from scripts.main_gui import Menu


class TexMenu:
    def __init__(self):
        
        btnClick = pygame.mixer.Sound("sounds\\menu-click.wav")
        
        def Change():
            Globals.map_scene = "editor"
            btnClick.play()
        
        window_width = 800
        
        btnGrass = Menu.BrushButton(text = "Grass", rect = (0,0, 64, 64), bg  = Color.Gray, fg = Color.White, bgr = Color.CornflowerBlue, tag = ("tex_menu", None))
        btnGrass.Left = window_width / 2 - btnGrass.Width / 2
        btnGrass.Top = 100
        btnGrass.Brush = "1"
        btnGrass.Command = Change
        
        btnStone = Menu.BrushButton(text = "Stone", rect = (0,0, 64, 64), bg  = Color.Gray, fg = Color.White, bgr = Color.CornflowerBlue, tag = ("tex_menu", None))
        btnStone.Left = window_width / 2 - btnStone.Width / 2
        btnStone.Top = 200
        btnStone.Brush = "2"
        btnStone.Command = Change
        
        btnWater = Menu.BrushButton(text = "Water", rect = (0,0, 64, 64), bg  = Color.Gray, fg = Color.White, bgr = Color.CornflowerBlue, tag = ("tex_menu", None))
        btnWater.Left = window_width / 2 - btnWater.Width / 2
        btnWater.Top = 300
        btnWater.Brush = "3"
        btnWater.Command = Change
        
        btnFence = Menu.BrushButton(text = "Fence", rect = (0,0, 64, 64), bg  = Color.Gray, fg = Color.White, bgr = Color.CornflowerBlue, tag = ("tex_menu", None))
        btnFence.Left = window_width / 2 - btnFence.Width / 2
        btnFence.Top = 400
        btnFence.Brush = "4"
        btnFence.Command = Change
        
        btnSand = Menu.BrushButton(text = "Sand", rect = (0,0, 64, 64), bg  = Color.Gray, fg = Color.White, bgr = Color.CornflowerBlue, tag = ("tex_menu", None))
        btnSand.Left = window_width / 2 - btnSand.Width / 2
        btnSand.Top = 500
        btnSand.Brush = "5"
        btnSand.Command = Change
        