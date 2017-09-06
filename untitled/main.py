'''
Created on Aug 31, 2017

@author: ddimarcello
'''

import sys, pygame, math
from scripts.globals import *
from scripts.map_engine import *
from scripts.NPC import *
from scripts.player import *

pygame.init()

clock = pygame.time.Clock()

terrain = Map_Engine.load_map("maps\\world.map")
pygame.display.set_caption("Boudicca")

fps_font = pygame.font.Font("C:\\Windows\\Fonts\\Verdana.ttf", 20)
fps = 1
deltatime = 1

sky = pygame.image.load("graphics\\sky.png")
Sky = pygame.Surface(sky.get_size(), pygame.HWSURFACE)
Sky.blit(sky, (0,0))
del sky

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
        
        
            
        
    #Logic
    if Globals.camera_move == 1:
        if not Tiles.Blocked_At((round(player_x), math.floor(player_y))):
            Globals.camera_y += deltatime * 300
    elif Globals.camera_move == 2:
        if not Tiles.Blocked_At((round(player_x), math.ceil(player_y))):
            Globals.camera_y -= deltatime * 300
    elif Globals.camera_move == 3:
        if not Tiles.Blocked_At((math.floor(player_x), round(player_y))):
            Globals.camera_x += deltatime * 300
    elif Globals.camera_move == 4:
        if not Tiles.Blocked_At((math.ceil(player_x), round(player_y))):
            Globals.camera_x -= deltatime * 300
    
    player_x = (window_width / 2 - player_w / 2 -  Globals.camera_x) / Tiles.Size
    player_y = (window_height / 2 - player_h / 2 -  Globals.camera_y) / Tiles.Size
    
    
    #Render Graphics        
    window.blit(Sky, (0,0))
    
    window.blit(terrain, (Globals.camera_x, Globals.camera_y))            
    
    player.render(window, (window_width / 2 - player_w / 2,
                           window_height / 2 - player_h / 2))
    
    
    
    show_fps()
    
    
    pygame.display.update()
    
    clock.tick()
    fps = clock.get_fps()
    deltatime = 1/(fps+1)
            
pygame.quit()
sys.exit()    