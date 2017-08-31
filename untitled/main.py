'''
Created on Aug 31, 2017

@author: ddimarcello
'''

import sys, pygame
from scripts.globals import *
from scripts.map_engine import *

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

isRunning = True

#events loop
while isRunning:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            isRunning = False
        
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_w:
                Globals.camera_move = 1
            elif event.key == pygame.K_s:
                Globals.camera_move = 2
            elif event.key == pygame.K_a:
                Globals.camera_move = 3
            elif event.key == pygame.K_d:
                Globals.camera_move = 4
                
        if event.type == pygame.KEYUP:
            Globals.camera_move = 0
        
        
            
        
    #Logic
    if Globals.camera_move == 1:
        Globals.camera_y += deltatime * 100
    elif Globals.camera_move == 2:
        Globals.camera_y -= deltatime * 100
    elif Globals.camera_move == 3:
        Globals.camera_x += deltatime * 100
    elif Globals.camera_move == 4:
        Globals.camera_x -= deltatime * 100
    
    
    #Render Graphics        
    window.blit(Sky, (0,0))
    
    window.blit(terrain, (Globals.camera_x, Globals.camera_y))            
    
    
    show_fps()
    
    
    pygame.display.update()
    
    clock.tick()
    fps = clock.get_fps()
    deltatime = 1/(fps+1)
            
pygame.quit()
sys.exit()    