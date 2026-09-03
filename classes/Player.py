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
from classes.Wall import Wall

########################################################################################################################
# Constants
########################################################################################################################

# Directions:
# 0 = North
# 1 = East
# 2 = South
# 3 = West
DIRECTIONS = (
    (0, 1),
    (1, 0),
    (0, -1),
    (-1, 0),
)
########################################################################################################################
# Class                                                                                                                #
########################################################################################################################
class Player:
    ### Constructor ###
    def __init__(self, pos_x,pos_y, pixel_size, tile_size, game_area):
        # Tile position
        self.grid_x = pos_x
        self.grid_y = pos_y

        # Pixel position
        self.x = (pos_x+0.5) * tile_size
        self.y = pos_y * tile_size

        # Movement
        self.pixel_size = pixel_size
        self.tile_size = tile_size
        self.game_area = game_area
        self.direction = None
        self.buffered_direction = None
        self.speed = tile_size / 16
        self.is_alive = True
        
        self.body = pygame.image.load("assets/sprites/player/pacman.png")


    ### Methods ###
    def draw(self, screen):
        offset = 3 * self.pixel_size

        draw_position = (
            self.x - offset,
            self.y + self.game_area - offset,
        )

        # Draw body unless the ghost is dead
        body = pygame.transform.scale_by(
            self.body,
            self.pixel_size,
        )
        screen.blit(body, draw_position)

    def move(self, board):
        self.check_new_direction(board)
        if self.direction is not None:
            dx, dy = DIRECTIONS[self.direction]

            self.x += dx * self.speed
            self.y += dy * self.speed

            self.wrap_position(board)

            # Change direction only when centered on a tile
            if self.x % self.tile_size == 0 and self.y % self.tile_size == 0:
                self.grid_x = int(self.x / self.tile_size)
                self.grid_y = int(self.y / self.tile_size)
                
                self.check_direction(board)

    def wrap_position(self, board):
        """Wrap the ghost around the edges of the board."""

        width = len(board[0]) * self.tile_size
        height = len(board) * self.tile_size

        if self.x >= width:
            self.x = 0
        elif self.x < 0:
            self.x = (len(board[0]) - 1) * self.tile_size

        if self.y >= height:
            self.y = 0
        elif self.y < 0:
            self.y = (len(board) - 1) * self.tile_size

    def check_new_direction(self, board):
        if self.buffered_direction is not None:
            dx, dy = DIRECTIONS[self.buffered_direction]
            print(self.grid_x + dx, self.grid_y + dy)
            if not isinstance(board[self.grid_y + dy][self.grid_x + dx], Wall):
                self.direction = self.buffered_direction
                self.buffered_direction = None
    
    def check_direction(self, board):
        dx, dy = DIRECTIONS[self.direction]
        if isinstance(board[self.grid_y + dy][self.grid_x + dx], Wall):
            self.direction = None