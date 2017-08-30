import pygame, sys
from textures import *

pygame.init()

clock = pygame.time.Clock()

tile_size = 32

fps_font = pygame.font.Font("C:\\Windows\\Fonts\\Verdana.ttf", 20)

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

while isRunning:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            isRunning = False
    
    #Logic
    clock.tick()
    fps = clock.get_fps()
    
    #Render Graphics        
    window.fill((0,0,0))
    
    # - Render Simple Terrain Grid
    for x in range(0, 800, tile_size):
        for y in range(0, 600, tile_size):
            window.blit(Tiles.Grass, (x,y))
    
    
    show_fps()
    
    
    pygame.display.update()
            
pygame.quit()
sys.exit()    