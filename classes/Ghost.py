#***********************************************************************************************************************
# Program name:         Ghost.py
# Description:          Class for Pac-Man ghosts
# Author:               Gatien Clerc
# Creation date:        25.08.2026
# Modified by:          -
# Modification date:    -
# Version:              0.1
#***********************************************************************************************************************
########################################################################################################################
# Imports                                                                                                              #
########################################################################################################################
import pygame
import random
from classes.Wall import Wall

########################################################################################################################
# Variable                                                                                                             #
########################################################################################################################
directions = [
    [0, 1], #n
    [1, 0], #e
    [0, -1],#s
    [-1, 0] #w
]

########################################################################################################################
# Class                                                                                                                #
########################################################################################################################
class Ghost:
    ### Attributes ###
    sprite = None

    ### Constructor ###
    def __init__(self, pos_x, pos_y, pixel_size=1, tile_size=8, game_area=24 , sprite=None):
        self.pos_x = pos_x
        self.pos_y = pos_y
        
        self.pixel_size = pixel_size
        self.tile_size = tile_size
        self.game_area = game_area
        self.sprite = sprite
        
        self.direction = 1
        self.speed = 2
        self.is_alive = True

    ### Methods ###
    def draw(self, screen):
        offset = 3*self.pixel_size
        screen.blit(pygame.transform.scale_by(self.sprite, self.pixel_size), (self.pos_x*self.tile_size-offset, self.pos_y*self.tile_size+self.game_area-offset))
  
    
    def move(self, x_lenght):
        self.pos_x = self.pos_x+directions[self.direction][0]%
        self.pos_y += directions[self.direction][1]


    def check_path(self, board):
        #       n  e  s  w
        path = [0, 0, 0, 0]
        
        for i in range(len(directions)):
            if not isinstance(board[self.pos_y+directions[i][1]][self.pos_x+directions[i][0]], Wall):
                path[i] = 1
        
        return path
    
    
    def ai(self, board):
        path = self.check_path(board)
        option = []
        for i in range(len(path)):
            if i != (self.direction + 2) % 4 and path[i] == 1:
                option.append(i)
        
        self.direction = random.choice(option)
        self.move()
        
                
        
  