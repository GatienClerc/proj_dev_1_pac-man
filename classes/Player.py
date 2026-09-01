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
    # TODO: Set new player sprite when player is moving
    SIZE = 12
    direction = None
    buffered_direction = None

    ### Constructor ###
    def __init__(self, pos_x,pos_y, pixel_size):
        self.pos_x = pos_x
        self.pos_y = pos_y

        self.sprite = pygame.image.load("assets/sprites/player/pacman.png")
        self.sprite = pygame.transform.scale_by(self.sprite, pixel_size)


    ### Methods ###
    def draw(self, screen):
        screen.blit(self.sprite, (self.pos_x, self.pos_y))

    def move(self, screen, one_pixel, one_tile, max_x, min_y, max_y):
        """
        Moves the player to the specified direction.

        :param screen: The game window
        :param one_pixel: The size of one pixel
        :param one_tile: The size of one tile
        :param max_x: The end of the game window horizontally
        :param min_y: The start of the game area within the game window vertically
        :param max_y: The end of the game area within the game window horizontally
        :return:
        """
        if not self.direction:
            if self.buffered_direction:
                self.direction = self.buffered_direction
                self.buffered_direction = None

            else: return

        elif self.direction == "up": self.pos_y -= one_pixel
        elif self.direction == "left": self.pos_x -= one_pixel
        elif self.direction == "down": self.pos_y += one_pixel
        elif self.direction == "right": self.pos_x += one_pixel

        if self.pos_y + self.SIZE * one_pixel <= min_y: self.pos_y += (max_y - min_y) + one_tile
        elif self.pos_x + self.SIZE * one_pixel <= 0: self.pos_x += max_x + one_tile
        elif self.pos_y >= max_y: self.pos_y -= (max_y - min_y) + self.SIZE * one_pixel
        elif self.pos_x >= max_x: self.pos_x -= max_x + self.SIZE * one_pixel

        self.draw(screen)


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