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
# 0 = South
# 1 = East
# 2 = North
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
WAIT = "wait"

# Ghost house positions
GHOST_HOME_IN = (13, 11)
GHOST_HOUSE_OUT = (13, 14)

#speed multiplier
SPEED_WAIT = 0
SPEED_NORMAL = 0.9
SPEED_SCARED = 0.625
SPEED_DEAD = 2

color_scared = [(0,0,255), (255,255,255)]

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
        self.x = (pos_x+0.5) * tile_size
        self.y = pos_y * tile_size

        # Movement
        self.pixel_size = pixel_size
        self.tile_size = tile_size
        self.game_area = game_area
        self.direction = 1
        self.speed = SPEED_WAIT
        self.is_alive = True

        # AI
        self.state = WAIT
        self.scatter_target = [0, 0]
        self.target = [0, 0]
        self.wait_time = 0
        self.wait_timer = 0
        
        self.scared_time = 6*60
        self.scared_timer = 0

        # Animation
        self.animation_frame = 0
        self.animation_delay = 20
        self.animation_delay_count = 0

        # Color
        self.main_color = color
        self.color = color

        # Sprites
        self.body = spritesheet(
            "assets/sprites/ghost/ghost_body.png",
            2,
            1,
            14,
            14,
        )

        self.eyes = spritesheet(
            "assets/sprites/ghost/ghost_eye.png",
            2,
            2,
            14,
            14,
        )
        
        self.scared_eyes = pygame.image.load("assets/sprites/ghost/ghost_eye_scared.png")

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
        if self.state not in (DEAD, GET_IN):
            
            body = []
            for i in range(len(self.body)):
                body.append(color_swap(
                    self.body[i],
                    (255, 0, 0),
                    self.color,
                ))
                
            new_body = pygame.transform.scale_by(
                body[self.animation_frame],
                self.pixel_size,
            )
            screen.blit(new_body, draw_position)

        # Draw eyes unless the ghost is scared
        if self.state != SCARED:
            eyes = pygame.transform.scale_by(
                self.eyes[self.direction],
                self.pixel_size,
            )
            screen.blit(eyes, draw_position)
        else:
            eyes = pygame.transform.scale_by(
                self.scared_eyes,
                self.pixel_size,
            )
            screen.blit(eyes, draw_position)

        self.update_animation()
        """
        #show target debug
        draw_position = (
            self.target[0]*self.tile_size - offset,
            self.target[1]*self.tile_size + self.game_area - offset,
        )
        body = pygame.transform.scale_by(
            self.body[self.animation_frame],
            self.pixel_size,
        )
        screen.blit(body, draw_position)
        """

    def update_animation(self):
        """Update the ghost animation."""

        self.animation_delay_count += 1

        if self.animation_delay_count < self.animation_delay:
            return

        self.animation_delay_count = 0
        self.animation_frame = (self.animation_frame + 1) % 2

        self.color = (
            color_scared[self.animation_frame]
            if self.state == SCARED
            else self.main_color
        )

    ####################################################################################################################
    # Movement
    ####################################################################################################################

    def move(self, board, player):
        """Move the ghost and update its direction when reaching a tile center."""
        if self.state == WAIT:
            self.wait_timer +=1
            if self.wait_timer >= self.wait_time:
                self.state = GET_OUT
                self.speed = self.pixel_size*SPEED_NORMAL

        self.scared_timer += 1
        
        dx, dy = DIRECTIONS[self.direction]

        # Move
        self.x += dx * self.speed
        self.y += dy * self.speed
        self.wrap_position(board)

        # Current tile
        center_x = self.x + self.tile_size / 2
        center_y = self.y + self.tile_size / 2

        self.grid_x = int(center_x // self.tile_size)
        self.grid_y = int(center_y // self.tile_size)

        tile_center_x = self.grid_x * self.tile_size + self.tile_size / 2
        tile_center_y = self.grid_y * self.tile_size + self.tile_size / 2

        # Check whether we've reached the center of the current tile
        distance = (
            abs(center_x - tile_center_x)
            if dx
            else abs(center_y - tile_center_y)
        )

        if distance < self.speed - 0.1:
            # Snap to the grid
            self.x = self.grid_x * self.tile_size
            self.y = self.grid_y * self.tile_size
            if self.state != WAIT:
                self.ai(board, player)

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
        """Return available movement directions."""

        available = [False] * 4

        height = len(board)
        width = len(board[0])

        for direction, (dx, dy) in enumerate(DIRECTIONS):
            next_x = (self.grid_x + dx) % width
            next_y = self.grid_y + dy

            if not (0 <= next_y < height):
                continue

            tile = board[next_y][next_x]

            if not isinstance(tile, Wall):
                available[direction] = True

            elif tile.is_gate and self.state in (GET_IN, GET_OUT):
                available[direction] = True

        return available

    def get_direction(self, directions):
        """Return the direction closest to the current target."""

        return min(
            directions,
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

    def chase(self, player):
        """Return the target position when chasing Pac-Man."""

        return [0, 0]

    def update_target(self, player):
        """Update target and speed according to state."""

        if self.state == SCATTER:
            self.speed = self.pixel_size * SPEED_NORMAL
            self.target = self.scatter_target

        elif self.state == CHASE:
            self.speed = self.pixel_size * SPEED_NORMAL
            self.target = self.chase(player)

        elif self.state == DEAD:
            self.speed = self.pixel_size * SPEED_DEAD
            self.target = list(GHOST_HOME_IN)

            if (self.grid_x, self.grid_y) == GHOST_HOME_IN:
                self.state = GET_IN

        elif self.state == GET_IN:
            self.target = list(GHOST_HOUSE_OUT)

            if (self.grid_x, self.grid_y) == GHOST_HOUSE_OUT:
                self.state = GET_OUT

        elif self.state == GET_OUT:
            self.speed = self.pixel_size * SPEED_NORMAL
            self.target = list(GHOST_HOME_IN)

            if self.grid_y <= GHOST_HOME_IN[1]:
                self.state = SCATTER

    def ai(self, board, player):
        """Choose the next movement direction."""

        available_paths = self.check_path(board)

        opposite_direction = (self.direction + 2) % 4

        valid_directions = [
            direction
            for direction in range(4)
            if available_paths[direction]
               and direction != opposite_direction
        ]

        if not valid_directions:
            self.direction = opposite_direction
            return

        if self.state == SCARED:
            self.speed = self.pixel_size * SPEED_SCARED
            self.direction = random.choice(valid_directions)

            if self.scared_timer >= self.scared_time:
                self.state = SCATTER

            return

        self.scared_timer = 0

        self.update_target(player)
        self.direction = self.get_direction(valid_directions)

    def change_state_to(self, new_state):
        """Change ghost state and reverse direction if required."""

        blocked_states = {
            DEAD,
            GET_IN,
            GET_OUT,
            WAIT,
            SCARED,
        }

        if self.state == new_state:
            return

        if self.state in blocked_states:
            return

        self.state = new_state
        self.direction = (self.direction + 2) % 4