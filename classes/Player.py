#***********************************************************************************************************************
# Program name:         Player.py
# Description:          Class for the Player object that the user will control
# Author:               Thierry Perroud
# Creation date:        20.08.2026
# Modified by:          -
# Modification date:    -
# Version:              0.1
#***********************************************************************************************************************
########################################################################################################################
# Imports                                                                                                              #
########################################################################################################################
import pygame

########################################################################################################################
# Class                                                                                                                #
########################################################################################################################
class Player:
    ### Attributes ###
    sprite = None

    ### Constructor ###
    def __init__(self, pos_x,pos_y):
        self.pos_x = pos_x
        self.pos_y = pos_y


    ### Methods ###
    def move(self, direction):
        """
        Moves the player to the specified direction.

        :param direction: Can be "up", "down", "left" or "right
        :return:
        """
        if direction == "up":
            self.pos_y -= 0.5

        elif direction == "down":
            self.pos_y += 0.5

        elif direction == "left":
            self.pos_x -= 0.5

        elif direction == "right":
            self.pos_x += 0.5


    def set_sprite(self, new_sprite):
        """
        Sets a new sprite to the Player object when the player is moving.

        :param new_sprite: The new sprite of the Player object
        :return:
        """
        # TODO: Set new player sprite when player is moving
        pass


    def set_position(self, pos_x, pos_y):
        """
        Teleports player into a new position on the game board.

        :param pos_x: new horizontal position of the player
        :param pos_y: new vertical position of the player
        :return:
        """
        self.pos_x = pos_x
        self.pos_y = pos_y