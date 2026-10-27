#***********************************************************************************************************************
# Program name:         Player.py
# Description:          Class for the Player object that the user will control
# Author:               Thierry Perroud
# Creation date:        20.08.2026
# Modified by:          Gatien Clerc
# Modification date:    15.09.2026
# Version:              0.5
#***********************************************************************************************************************
########################################################################################################################
# Imports                                                                                                              #
########################################################################################################################
import pygame
from classes.Wall import Wall
from utils.spritesheet import spritesheet

########################################################################################################################
# Constants
########################################################################################################################

# Directions:
DIRECTIONS = (
    (0, 1),     # South
    (1, 0),     # East
    (0, -1),    # North
    (-1, 0),    # West
)

#direction -> rotation
ROTATIONS = {
    0 : 270,
    1 : 0,
    2 : 90,
    3 : 180,
}


dot_points = 10
power_up = 40
ghost_points = 200
########################################################################################################################
# Class                                                                                                                #
########################################################################################################################
class Player:
    ### Constructor ###
    def __init__(self, pos_x,pos_y, pixel_size, tile_size, game_area):
        # Tile position
        self.grid_x = pos_x
        self.grid_y = pos_y
        self.respawn_position = [self.grid_x, self.grid_y]

        # Pixel position
        self.x = (pos_x+0.5) * tile_size
        self.y = pos_y * tile_size
        self.respawn_point = [self.x, self.y]

        # Movement
        self.pixel_size = pixel_size
        self.tile_size = tile_size
        self.game_area = game_area
        self.last_direction = 0
        self.direction = None
        self.buffered_direction = None
        self.speed = pixel_size
        self.is_alive = True
        
        self.is_dying = False
        
        # animation
        self.body = spritesheet("assets/sprites/player/pacman_move.png", 1, 4, 14, 14)
        self.animation_frame = 0
        self.animation_delay = 5
        self.animation_delay_count = 0
        
        self.body_die = spritesheet("assets/sprites/player/pacman_die.png", 3, 4, 15, 16)
        self.animation_die_frame = 0
        self.animation_die_delay = 8
        self.animation_die_delay_count = 0

        self.life_count = 2
        self.score = 0
        self.dot_count = 0

    ### Methods ###
    def draw(self, screen):
        offset = 3 * self.pixel_size
        draw_position = (
            self.x - offset,
            self.y + self.game_area - offset,
        )
        
        if not self.is_dying:
    
            # Draw body unless the ghost is dead
            body = pygame.transform.scale_by(
                self.body[self.animation_frame],
                self.pixel_size,
            )
            body = pygame.transform.rotate(body, ROTATIONS[self.last_direction])
            
            if self.direction is not None:
                self.update_animation()
        else:
            body = pygame.transform.scale_by(
                self.body_die[self.animation_die_frame],
                self.pixel_size,
            )
            self.update_death_animation()
        
        screen.blit(body, draw_position)


    def update_animation(self):
        """Update the player animation."""

        self.animation_delay_count += 1

        if self.animation_delay_count < self.animation_delay:
            return

        self.animation_delay_count = 0
        self.animation_frame = (self.animation_frame + 1) % len(self.body)


    def update_death_animation(self):
        self.animation_die_delay_count += 1

        if self.animation_die_delay_count < self.animation_die_delay:
            return

        if self.animation_die_frame >= len(self.body_die)-1:
            self.animation_die_frame = 0
            self.is_dying = False
            self.is_alive = False
            return
        
        self.animation_die_delay_count = 0
        self.animation_die_frame += 1


    def move(self, board, ghosts):
        if self.direction is not None:
            dx, dy = DIRECTIONS[self.direction]

            self.x += dx * self.speed
            self.y += dy * self.speed

            self.wrap_position(board)

            # Change direction only when centered on a tile
            if self.x % self.tile_size == 0 and self.y % self.tile_size == 0:
                self.grid_x = int(self.x / self.tile_size)
                self.grid_y = int(self.y / self.tile_size)
                
                self.check_new_direction(board)
                self.check_direction(board)

        elif self.buffered_direction is not None:
            self.check_new_direction(board)

        self.get_collectibles(board, ghosts)
        
        self.check_ghosts(ghosts)


    def wrap_position(self, board):
        """Wrap the ghost around the edges of the board."""

        width = (len(board[0])-1) * self.tile_size
        height = (len(board)-1) * self.tile_size

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
            if not isinstance(board[self.grid_y + dy][self.grid_x + dx], Wall):
                self.direction = self.buffered_direction
                self.last_direction = self.buffered_direction
                self.buffered_direction = None


    def check_direction(self, board):
        dx, dy = DIRECTIONS[self.direction]
        if isinstance(board[self.grid_y + dy][self.grid_x + dx], Wall):
            self.direction = None


    def get_collectibles(self, board, ghosts):
        if not board[self.grid_y][self.grid_x].item_type: return
        if board[self.grid_y][self.grid_x].item_type == "Power Up": self.power_up(ghosts)

        board[self.grid_y][self.grid_x].remove_item()
        self.dot_count -= 1
        self.score += dot_points


    def power_up(self, ghosts):
        self.score += power_up
        
        for ghost in ghosts:
            if ghost.state in ("chase", "scatter", "scared"):
                ghost.state = "scared"
                ghost.scared_timer = 0
                ghost.direction = (ghost.direction + 2) % 4

    def check_ghosts(self, ghosts):
        player_rect = pygame.Rect(
            self.x - self.pixel_size,
            self.y + self.game_area - self.pixel_size,
            self.pixel_size * 8,
            self.pixel_size * 8
        )

        for ghost in ghosts:
            ghost_rect = pygame.Rect(
                ghost.x - self.pixel_size,
                ghost.y + self.game_area - self.pixel_size,
                self.pixel_size * 8,
                self.pixel_size * 8
            )

            if player_rect.colliderect(ghost_rect):
                if ghost.state != "dead":
                    if ghost.state == "scared":
                        ghost.state = "dead"
                        self.score += ghost_points
                    else:
                        self.is_dying = True


    def respawn_player(self):
        self.grid_x, self.grid_y = self.respawn_position[0], self.respawn_position[1]
        self.x, self.y = self.respawn_point[0], self.respawn_point[1]
        self.last_direction = 0
        self.direction = None
        self.buffered_direction = None
        self.is_alive = True
        self.animation_frame = 0