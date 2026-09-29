#***********************************************************************************************************************
# Program name:         game.py
# Description:          the game screen
# Author:               Cédric Jankiewicz
# Creation date:        23.08.2026
# Modified by:          Gatien Clerc
# Modification date:    15.09.26
# Version:              1.0
#***********************************************************************************************************************
from utils.read_gamedata import read_gamedata
from utils.wall_tileset import set_wall_image
from classes.Ground import Ground

global_ghosts_state = "scatter"
global_ghosts_timer = 0
global_ghosts_cycle = 0
state_time = [7,20,7,20,5,20,5]

ready_time = 2*60
ready_timer = 0

def game_innit(game_area, tile_size, pixel_size):
    board, player, ghosts = read_gamedata(tile_size, game_area, pixel_size)
    set_wall_image(board, pixel_size)

    for row in board:
        for tile in row:
            if isinstance(tile, Ground) :
                if tile.item_type in ("Dot", "Power Up"):
                    player.dot_count += 1

    return board, player, ghosts


def game_screen(screen, board, font, tile_size, player, ghosts):
    global ready_timer
    if ready_timer >= ready_time: 
        #logic
        player.move(board, ghosts)
        
        for ghost in ghosts:
            ghost.move(board, player)
        update_ghosts(ghosts)
        
    else:
        #ready and timer
        ready_timer += 1
        text_ready = font.render(f"READY!", True, ('yellow'))
        text_rect = text_ready.get_rect(center=(tile_size * 14, tile_size * 20.5))
        screen.blit(text_ready, text_rect)
    
    #draw
    draw_board(screen, board)
    draw_score(screen, font, player.life_count, player.score, tile_size)
    
    player.draw(screen)
    
    for ghost in ghosts:
        ghost.draw(screen)


def draw_board(screen, board):
    for col in board:
        for tile in col:
            tile.draw(screen)


def update_ghosts(ghosts):
    global global_ghosts_state
    global global_ghosts_timer
    global global_ghosts_cycle
    
    # stop cycling after finishing the cycles
    if global_ghosts_cycle < len(state_time):
        global_ghosts_timer += 1

        if global_ghosts_timer >= state_time[global_ghosts_cycle] * 60:
            global_ghosts_timer = 0
            global_ghosts_cycle += 1

            if global_ghosts_state == "scatter":
                global_ghosts_state = "chase"
            else:
                global_ghosts_state = "scatter"

    else:
        global_ghosts_state = "chase"

    for ghost in ghosts:
        ghost.change_state_to(global_ghosts_state)


def reset_entities(player, ghosts):
    global global_ghosts_state, global_ghosts_timer, global_ghosts_cycle_num, ready_timer
    player.respawn_player()

    for ghost in ghosts:
        ghost.reset_ghost()
        ghost.reset_red_state()

    global_ghosts_state = "scatter"
    global_ghosts_timer = 0
    global_ghosts_cycle_num = 0
    
    ready_timer = 0
    
    
def draw_score(screen, font,life_count, score, tile_size):
    text_1up = font.render(f"{life_count}UP", True, ('white'))
    screen.blit(text_1up, (tile_size * 3, 0))

    text_2up = font.render(f"HIGH SCORE", True, ('white'))
    screen.blit(text_2up, (tile_size * 9, 0))

    text = font.render(f"{score}", True, ('white'))
    screen.blit(text, (tile_size * 12, tile_size))
