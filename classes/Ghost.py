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

########################################################################################################################
# Class                                                                                                                #
########################################################################################################################
class Ghost:
    ### Attributes ###
    sprite = None

    ### Constructor ###
    def __init__(self, pos_x, pos_y, sprite=None):
        self.pos_x = pos_x
        self.pos_y = pos_y

        self.sprite = sprite
        self.speed = 2
        self.is_alive = True

    ### Methods ###
    def move(self, direction):
        """
        Moves the player to the specified direction.

        :param direction: Can be "up", "down", "left" or "right
        :return:
        """
        if self.direction == "up":
            self.pos_y -= self.speed

        elif self.direction == "down":
            self.pos_y += self.speed

        elif self.direction == "left":
            self.pos_x -= self.speed

        elif self.direction == "right":
            self.pos_x += self.speed

    def set_direction(self, direction):
        """
        Changes ghost direction.
        """

        valid_directions = ["up", "down", "left", "right"]

        if direction in valid_directions:
            self.direction = direction


    def set_sprite(self, new_sprite):
        """
        Sets a new sprite to the Ghost object when the Ghost is moving.

        :param new_sprite: The new sprite of the Ghost object
        :return:
        """
        # TODO: Set new Ghost sprite when Ghost is moving
        # self.sprite = new_sprite


    def set_position(self, pos_x, pos_y):
        """
        Teleports Ghost into a new position on the game board.

        :param pos_x: new horizontal position of the Ghost
        :param pos_y: new vertical position of the Ghost
        :return:
        """
        self.pos_x = pos_x
        self.pos_y = pos_y

    def behavior(self):
        pass
