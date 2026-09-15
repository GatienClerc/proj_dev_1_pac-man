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

    ### Constructor ###
    def __init__(self,pos_x,pos_y, pixel_size, is_gate=False):
        super().__init__(pos_x,pos_y,pixel_size)
        
        self.image = pygame.Surface((pixel_size, pixel_size), pygame.SRCALPHA)
        self.image.fill((0, 0, 0, 0))
        self.is_gate = is_gate
    
    def draw(self, screen):
        screen.blit(pygame.transform.scale_by(self.image, self.pixel_size), (self.pos_x, self.pos_y))
        