# **********************************************************************************************************************
# Program name:         Ghost.py
# Description:          Class for Pac-Man ghosts
# Author:               Gatien Clerc
# Creation date:        25.08.2026
# Modified by:          Cédric Jankiewicz
# Modification date:   01.09.2026
# Version:              0.3
# **********************************************************************************************************************

########################################################################################################################
# Imports
########################################################################################################################

import math
import random

import pygame

from classes.Wall import Wall
from utils.color_swap import color_swap
from utils.spritesheet import spritesheet


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

# Ghost states
SCATTER = "scatter"
CHASE = "chase"
SCARED = "scared"
DEAD = "dead"
GET_IN = "get_in"
GET_OUT = "get_out"

# Ghost house positions
GHOST_HOME_IN = (14, 11)
GHOST_HOUSE_OUT = (14, 14)


########################################################################################################################
# Class
########################################################################################################################

class Ghost:
    def __init__(
        self,
        pos_x,
        pos_y,
        pixel_size=1,
        tile_size=8,
        game_area=24,
        color=(255, 0, 0),
    ):
        # Tile position
        self.grid_x = pos_x
        self.grid_y = pos_y

        # Pixel position
        self.x = pos_x * tile_size
        self.y = pos_y * tile_size

        # Movement
        self.pixel_size = pixel_size
        self.tile_size = tile_size
        self.game_area = game_area
        self.direction = 1
        self.speed = tile_size / 16
        self.is_alive = True

        # AI
        self.state = GET_OUT
        self.scatter_target = [0, 0]
        self.target = [0, 0]

        # Animation
        self.animation_frame = 0
        self.animation_delay = 10
        self.animation_delay_count = 0

        # Color
        self.color = color

        # Sprites
        self.body = spritesheet(
            "assets/sprites/ghost/ghost_body.png",
            2,
            1,
            14,
            14,
        )

        for i in range(len(self.body)):
            self.body[i] = color_swap(
                self.body[i],
                (255, 0, 0),
                self.color,
            )

        self.eyes = spritesheet(
            "assets/sprites/ghost/ghost_eye.png",
            2,
            2,
            14,
            14,
        )

    ####################################################################################################################
    # Drawing
    ####################################################################################################################

    def draw(self, screen):
        """Draw the ghost on the screen."""

        offset = 3 * self.pixel_size

        draw_position = (
            self.x - offset,
            self.y + self.game_area - offset,
        )

        # Draw body unless the ghost is dead
        if self.state != DEAD:
            body = pygame.transform.scale_by(
                self.body[self.animation_frame],
                self.pixel_size,
            )
            screen.blit(body, draw_position)

        # Draw eyes unless the ghost is scared
        if self.state != SCARED:
            eyes = pygame.transform.scale_by(
                self.eyes[self.direction],
                self.pixel_size,
            )
            screen.blit(eyes, draw_position)

        self.update_animation()

    def update_animation(self):
        """Update the ghost's animation frame."""

        self.animation_delay_count += 1

        if self.animation_delay_count >= self.animation_delay:
            self.animation_delay_count = 0
            self.animation_frame = (self.animation_frame + 1) % 2

    ####################################################################################################################
    # Movement
    ####################################################################################################################

    def move(self, board):
        """Move the ghost and update its direction at the center of a tile."""

        dx, dy = DIRECTIONS[self.direction]

        self.x += dx * self.speed
        self.y += dy * self.speed

        self.wrap_position(board)

        # Change direction only when centered on a tile
        if self.x % self.tile_size == 0 and self.y % self.tile_size == 0:
            self.grid_x = int(self.x / self.tile_size)
            self.grid_y = int(self.y / self.tile_size)

            self.ai(board)

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

    ####################################################################################################################
    # Pathfinding
    ####################################################################################################################

    def check_path(self, board):
        """Return the available directions from the current tile."""

        paths = [False] * 4

        height = len(board)
        width = len(board[0])

        for direction, (dx, dy) in enumerate(DIRECTIONS):
            x = (self.grid_x + dx) % width
            y = self.grid_y + dy

            # Ignore positions outside the board vertically
            if not 0 <= y < height:
                continue

            tile = board[y][x]

            # Normal walkable tile
            if not isinstance(tile, Wall):
                paths[direction] = True

            # Ghost gate can only be crossed while entering/leaving
            elif tile.is_gate and self.state in (GET_IN, GET_OUT):
                paths[direction] = True

        return paths

    def get_direction(self, paths):
        """Choose the direction that gets closest to the target."""

        return min(
            paths,
            key=lambda direction: math.dist(
                (
                    self.grid_x + DIRECTIONS[direction][0],
                    self.grid_y + DIRECTIONS[direction][1],
                ),
                self.target,
            ),
        )

    ####################################################################################################################
    # AI
    ####################################################################################################################

    def chase(self):
        """Return the target position when chasing Pac-Man."""

        return [0, 0]

    def update_target(self):
        """Update the ghost's target and state."""

        if self.state == SCATTER:
            self.target = self.scatter_target

        elif self.state == CHASE:
            self.target = self.chase()

        elif self.state == DEAD:
            self.target = list(GHOST_HOME_IN)

            if (self.grid_x, self.grid_y) == GHOST_HOME_IN:
                self.state = GET_IN

        elif self.state == GET_IN:
            self.target = list(GHOST_HOUSE_OUT)

            if self.grid_y >= GHOST_HOUSE_OUT[1]:
                self.state = GET_OUT

        elif self.state == GET_OUT:
            self.target = list(GHOST_HOME_IN)

            if self.grid_y <= GHOST_HOME_IN[1]:
                self.state = SCATTER

    def ai(self, board):
        """Choose the next direction for the ghost."""

        paths = self.check_path(board)

        # Prevent the ghost from immediately turning around
        opposite_direction = (self.direction + 2) % 4

        options = [
            direction
            for direction in range(4)
            if paths[direction] and direction != opposite_direction
        ]

        # If there is no other option, turn around
        if not options:
            self.direction = opposite_direction
            return

        # Scared ghosts choose a random available direction
        if self.state == SCARED:
            self.direction = random.choice(options)
            return

        # Update target according to the current state
        self.update_target()

        # Choose the direction closest to the target
        self.direction = self.get_direction(options)