import pygame, sys, time
from pip._vendor.pyparsing import White

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
    for x in range(0, 640, tile_size):
        for y in range(0, 480, tile_size):
            pygame.draw.rect(window, (255,255,0), (x, y, tile_size + 1, tile_size + 1), 1)
    
    
    show_fps()
    
    
    pygame.display.update()
            
pygame.quit()
sys.exit()    