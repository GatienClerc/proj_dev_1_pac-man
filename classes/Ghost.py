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
    def __init__(self, pos_x, pos_y, pixel_size=1, tile_size=8, game_area=24, sprite=None):

        # Tile position
        self.grid_x = pos_x
        self.grid_y = pos_y

        # Pixel position (float for smooth movement)
        self.x = pos_x * tile_size
        self.y = pos_y * tile_size

        self.pixel_size = pixel_size
        self.tile_size = tile_size
        self.game_area = game_area
        self.sprite = sprite

        self.direction = 1
        self.speed = 2  # pixels per frame
        self.is_alive = True


    def draw(self, screen):
        offset = 3 * self.pixel_size

        screen.blit(
            pygame.transform.scale_by(self.sprite, self.pixel_size),
            (
                self.x - offset,
                self.y + self.game_area - offset
            )
        )

    ### Move ###
    def move(self, board):

        dx, dy = directions[self.direction]

        self.x += dx * self.speed
        self.y += dy * self.speed

        # Wrap horizontally
        width = len(board[0])

        if self.x >= width * self.tile_size:
            self.x = 0

        elif self.x < 0:
            self.x = (width - 1) * self.tile_size

        # Wrap vertically
        height = len(board)

        if self.y >= height * self.tile_size:
            self.y = 0

        elif self.y < 0:
            self.y = (height - 1) * self.tile_size

        # When centered on a tile
        if self.x % self.tile_size == 0 and self.y % self.tile_size == 0:

            self.grid_x = int(self.x / self.tile_size)
            self.grid_y = int(self.y / self.tile_size)

            self.ai(board)


    def check_path(self, board):

        path = [0, 0, 0, 0]

        height = len(board)
        width = len(board[0])

        for i, (dx, dy) in enumerate(directions):

            x = (self.grid_x + dx) % width
            y = self.grid_y + dy

            if 0 <= y < height:

                if not isinstance(board[y][x], Wall):
                    path[i] = 1

        return path


    def ai(self, board):

        path = self.check_path(board)

        options = []

        # Don't reverse unless it's the only choice
        for i in range(4):

            if i != (self.direction + 2) % 4 and path[i]:
                options.append(i)

        if not options:
            self.direction = (self.direction + 2) % 4
        else:
            self.direction = random.choice(options)