#***********************************************************************************************************************
# Program name:         Wall.py
# Description:          Child tile class for wall tiles
# Author:               Thierry Perroud
# Creation date:        18.08.2026
# Modified by:          Cédric Jankiewicz
# Modification date:    25.08.2026
# Version:              0.2
#***********************************************************************************************************************
########################################################################################################################
# Imports                                                                                                              #
########################################################################################################################
import pygame
from classes.Tile import Tile

########################################################################################################################
# Class                                                                                                                #
########################################################################################################################
class Wall(Tile):
    """
    Wall tile class
    """
    ### Attributes ###
    # TODO: Set the image depending on adjacent walls when building the level

    ### Constructor ###
    def __init__(self,pos_x,pos_y,pixel_size):
        super().__init__(pos_x,pos_y,pixel_size)
        
        self.image = pygame.image.load("assets/sprites/terrain/wall.png")
        self.image = pygame.transform.scale(self.image, (8*pixel_size,8*pixel_size))
    
    def draw(self, screen):
        screen.blit(self.image, (self.pos_x, self.pos_y))
        