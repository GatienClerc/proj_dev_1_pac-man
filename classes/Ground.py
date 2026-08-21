#***********************************************************************************************************************
# Program name:         Ground.py
# Description:          Child tile class for ground tiles
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
class Ground(Tile):
    """
    Ground tile class
    """
    ### Constructor ###
    def __init__(self,pos_x,pos_y, has_item = True, item_type = None):
        super().__init__(pos_x,pos_y)
        self.has_item = has_item
        self.item_type = item_type

    ### Methods ###
    def draw_item(self):
        """
        draw_item draws an item on the ground tile depending on the item type.

        :return:
        """
        if not self.has_item: return
        if not self.item_type: return

        if self.item_type == "Dot":
            # TODO: Draw a Dot item in the center of the tile
            pass

        elif self.item_type == "Power Up":
            # TODO: Draw a Power Up item in the center of the tile
            pass

    def remove_item(self):
        """
        undraw_item removes the item on the ground tile when the player goes on the tile.

        :return:
        """
        self.has_item = False
        self.item_type = None

        # TODO: Visually remove the item that was collected