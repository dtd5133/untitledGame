'''
Created on Sep 6, 2017

@author: ddimarcello
'''

import pygame, random
from scripts.Timer import Timer
from scripts.globals import Globals

pygame.init()

def get_faces(sprite):
    
    faces = {}
    
    size = sprite.get_size()
    tile_size = (int(size[0] / 2), int(size[1] / 2))
    
    south = pygame.Surface(tile_size, pygame.HWSURFACE|pygame.SRCALPHA)
    south.blit(sprite, (0,0), (0,0, tile_size[0], tile_size[1]))
    faces["south"] = south
    
    north = pygame.Surface(tile_size, pygame.HWSURFACE|pygame.SRCALPHA)
    north.blit(sprite, (0,0), (tile_size[0], tile_size[1], tile_size[0], tile_size[1]))
    faces["north"] = north
    
    east = pygame.Surface(tile_size, pygame.HWSURFACE|pygame.SRCALPHA)
    east.blit(sprite, (0,0), (tile_size[0], 0, tile_size[0], tile_size[1]))
    faces["east"] = east
    
    west = pygame.Surface(tile_size, pygame.HWSURFACE|pygame.SRCALPHA)
    west.blit(sprite, (0,0), (0, tile_size[1], tile_size[0], tile_size[1]))
    faces["west"] = west
    
    return faces

def MoveNPC(npc):
    npc.facing = random.choice(("south", "north", "east", "west"))
    npc.walking = random.choice((True, False))


class NPC:
    
    AllNPCs = []
    
    def __init__(self, name, pos, dialog, sprite):
        self.Name = name
        self.X = pos[0]
        self.Y = pos[1]
        self.Dialog = dialog
        self.width = sprite.get_width()
        self.height = sprite.get_height()
        self.walking = False
        self.Timer = Timer(1)
        self.Timer.OnNext = lambda: MoveNPC(self)
        self.Timer.Start()
        
        #Get NPC faces
        self.facing = "south"
        self.faces = get_faces(sprite)
        
        #Publish
        NPC.AllNPCs.append(self)
    
    def Render(self, surface):
        self.Timer.Update()
        if self.walking:
            move_speed = 100 * Globals.deltatime
            if self.facing == "south":
                self.Y += move_speed
            elif self.facing == "north":
                self.Y -= move_speed
            elif self.facing == "east":
                self.X -= move_speed
            elif self.facing == "west":
                self.X += move_speed
        
        surface.blit(self.faces[self.facing], (self.X + Globals.camera_x, self.Y + Globals.camera_y))    
    
class Male1(NPC):
    def __init__(self, name, pos, dialog = None):
        super().__init__(name, pos, dialog, pygame.image.load("Graphics\\NPC\\male1.png"))
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        