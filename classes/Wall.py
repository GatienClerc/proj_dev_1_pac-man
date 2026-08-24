#***********************************************************************************************************************
# Program name:         Wall.py
# Description:          Child tile class for wall tiles
# Author:               Thierry Perroud
# Creation date:        18.08.2026
# Modified by:          -
# Modification date:    -
# Version:              0.1
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
    def __init__(self,pos_x,pos_y):
        super().__init__(pos_x,pos_y)
        
        self.image = pygame.image.load("assets/sprites/terrain/wall.png")
        self.image = pygame.transform.scale(self.image, (24,24))
    
    def draw(self, screen):
        screen.blit(self.image, (self.pos_x, self.pos_y))
        