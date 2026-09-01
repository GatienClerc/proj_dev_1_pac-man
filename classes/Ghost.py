#***********************************************************************************************************************
# Program name:         Ghost.py
# Description:          Class for Pac-Man ghosts
# Author:               Gatien Clerc
# Creation date:        25.08.2026
# Modified by:          Cédric Jankiewicz
# Modification date:    01.09.2026
# Version:              0.3
#***********************************************************************************************************************
########################################################################################################################
# Imports                                                                                                              #
########################################################################################################################
import pygame
import random
from classes.Wall import Wall
from utils.spritesheet import spritesheet
from utils.color_swap import color_swap

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
    def __init__(self, pos_x, pos_y, pixel_size=1, tile_size=8, game_area=24, color=(255,0,0)):

        # Tile position
        self.grid_x = pos_x
        self.grid_y = pos_y

        # Pixel position
        self.x = pos_x * tile_size
        self.y = pos_y * tile_size

        self.pixel_size = pixel_size
        self.tile_size = tile_size
        self.game_area = game_area
        
        self.direction = 1
        self.speed = tile_size/16
        self.is_alive = True
        
        # visuals
        self.animation_frame = 0
        self.animation_delay = 10
        self.animation_delay_count = 0
        
        self.color = color
        
        self.body = spritesheet("assets/sprites/ghost/ghost_body.png", 2, 1, 14, 14)
        for i in range(len(self.body)):
            self.body[i] = color_swap(self.body[i], (255,0,0), self.color)
            
        self.eyes = spritesheet("assets/sprites/ghost/ghost_eye.png", 2, 2, 14, 14)


    def draw(self, screen):
        """
        draw itself
        """
        offset = 3 * self.pixel_size

        screen.blit(
            pygame.transform.scale_by(self.body[self.animation_frame], self.pixel_size),
            (
                self.x - offset,
                self.y + self.game_area - offset
            )
        )
        screen.blit(
            pygame.transform.scale_by(self.eyes[self.direction], self.pixel_size),
            (
                self.x - offset,
                self.y + self.game_area - offset
            )
        )
        self.animation_delay_count += 1
        if self.animation_delay_count >= self.animation_delay:
            self.animation_delay_count = 0
            self.animation_frame = (self.animation_frame+1)%2


    def move(self, board):
        """
        move smoothly and check for direction when in the center of a tile
        """

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
        """
        get all possible path from the object position
        """

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
        """
        choice of the path it'll take (brain)
        """

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