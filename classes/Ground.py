#***********************************************************************************************************************
# Program name:         Ground.py
# Description:          Child tile class for ground tiles
# Author:               Thierry Perroud
# Creation date:        18.08.2026
# Modified by:          Cedric Jankiewicz
# Modification date:    27.08.2026
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

#images
dot = pygame.image.load("assets/sprites/collectables/dot.png")
power_up = pygame.image.load("assets/sprites/collectables/big_dot.png")

class Ground(Tile):
    """
    Ground tile class
    """
    ### Constructor ###
    def __init__(self,pos_x, pos_y, pixel_size, item_type = None, is_ghost_area = False):
        super().__init__(pos_x,pos_y,pixel_size)
        self.item_type = item_type
        self.is_ghost_area = is_ghost_area

    ### Methods ###
    def draw(self, screen):
        """
        draw draws an item on the ground tile depending on the item type.

        :return:
        """
        if not self.item_type: return

        if self.item_type == "Dot":
            screen.blit(pygame.transform.scale_by(dot, self.pixel_size), (self.pos_x, self.pos_y))

        elif self.item_type == "Power Up":
            screen.blit(pygame.transform.scale_by(power_up, self.pixel_size), (self.pos_x, self.pos_y))

    def remove_item(self):
        """
        remove_item removes the item on the ground tile

        :return:
        """
        self.item_type = None