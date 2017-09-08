'''
Created on Aug 31, 2017

@author: ddimarcello
'''

import sys, pygame, math
from scripts.globals import *
from scripts.map_engine import *
from scripts.NPC import *
from scripts.player import *
from scripts.main_gui import *

pygame.init()

clock = pygame.time.Clock()

terrain = Map_Engine.load_map("maps\\world.map")
pygame.display.set_caption("Boudicca")

fps_font = pygame.font.Font("C:\\Windows\\Fonts\\Verdana.ttf", 20)
fps = 0

sky = pygame.image.load("graphics\\sky.png")
Sky = pygame.Surface(sky.get_size(), pygame.HWSURFACE)
Sky.blit(sky, (0,0))
del sky

logo_img_temp = pygame.image.load("graphics\\logo.png")
logo_img = pygame.Surface(logo_img_temp.get_size(), pygame.HWSURFACE)
logo_img.blit(logo_img_temp, (0,0))
del logo_img_temp

def show_fps():
    fps_overlay = fps_font.render(str(int(fps)), True, (255,255,255))
    window.blit(fps_overlay, (0,0))

def createWindow():
    global window, window_height, window_width, window_title
    window_width, window_height = 800,600
    window_title = "untitled"
    window = pygame.display.set_mode((window_width, window_height), pygame.HWSURFACE|pygame.DOUBLEBUF)


createWindow()


player = Player("Boudicca")
player_w, player_h = player.width, player.height
player_x = (window_width / 2 - player_w / 2 -  Globals.camera_x)
player_y = (window_height / 2 - player_h / 2 -  Globals.camera_y)

man1 = Male1(name = "Eoin", pos = (200, 300))
man2 = Male1(name = "Ryan", pos = (260, 300))


#Initialize GUI

def Play():
    Globals.scene = "game"

def Exit():
    global isRunning
    isRunning = False

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

menuTitle = Menu.Text(text = "Boudicca", color = Color.Cyan, font = Font.Large)

logo = Menu.Image(bitmap = logo_img)


menuTitle.Left, menuTitle.Top = window_width / 2 - menuTitle.Width / 2, 0

isRunning = True

#events loop
while isRunning:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            isRunning = False
        
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_w:
                Globals.camera_move = 1
                player.facing = "north"
            elif event.key == pygame.K_s:
                Globals.camera_move = 2
                player.facing = "south"
            elif event.key == pygame.K_a:
                Globals.camera_move = 3
                player.facing = "east"
            elif event.key == pygame.K_d:
                Globals.camera_move = 4
                player.facing = "west"
                
        if event.type == pygame.KEYUP:
            Globals.camera_move = 0
        
        elif event.type == pygame.MOUSEBUTTONDOWN:
            if event.button == 1:    #LEFT CLICK
                
                #Handle button click events
                for btn in Menu.Button.All:
                    if btn.Tag[0] == Globals.scene and btn.Rolling:
                        if btn.Command != None:
                            btn.Command()   #Do button event
                        btn.Rolling = False
                        break   #Exit Loop
        
    #Render scene    
    if Globals.scene == "game":
        
        #Logic
        if Globals.camera_move == 1:
            if not Tiles.Blocked_At((round(player_x), math.floor(player_y))):
                Globals.camera_y += Globals.deltatime * 300
        elif Globals.camera_move == 2:
            if not Tiles.Blocked_At((round(player_x), math.ceil(player_y))):
                Globals.camera_y -= Globals.deltatime * 300
        elif Globals.camera_move == 3:
            if not Tiles.Blocked_At((math.floor(player_x), round(player_y))):
                Globals.camera_x += Globals.deltatime * 300
        elif Globals.camera_move == 4:
            if not Tiles.Blocked_At((math.ceil(player_x), round(player_y))):
                Globals.camera_x -= Globals.deltatime * 300
        
        player_x = (window_width / 2 - player_w / 2 -  Globals.camera_x) / Tiles.Size
        player_y = (window_height / 2 - player_h / 2 -  Globals.camera_y) / Tiles.Size
        
        
        #Render Graphics        
        window.blit(Sky, (0,0))
        
        window.blit(terrain, (Globals.camera_x, Globals.camera_y))            
        
        player.render(window, (window_width / 2 - player_w / 2,
                               window_height / 2 - player_h / 2))
    
        for npc in NPC.AllNPCs:
            npc.Render(window)
    
    
    #Process Menu
    elif Globals.scene == "menu":
        window.fill(Color.Fog)
        
        logo.Render(window)
        menuTitle.Render(window)
        
        for btn in Menu.Button.All:
            if btn.Tag[0] == "menu":
                
                btn.Render(window)
                
    
    
    show_fps()
    
    
    pygame.display.update()
    
    clock.tick()
    fps = clock.get_fps()
    Globals.deltatime = 1/(fps+1)
            
pygame.quit()
sys.exit()    