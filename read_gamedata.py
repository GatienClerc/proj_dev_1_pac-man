from classes.Ground import Ground
from classes.Wall import Wall

def read_gamedata(tile_size, game_area):
    file_path = "gamedata/board.txt"
    board = []

    with open(file_path, "r") as f:
        count_row = 0
        for line in f:
            row = []
            count_col = 0
            for char in line.rstrip("\n"):
                if char == "*":
                    row.append(Wall(game_area+tile_size*count_row, game_area+tile_size*count_col))
                else:
                    #TODO check all posibilities
                    row.append(Ground(game_area+tile_size*count_row, game_area+tile_size*count_col, False, False))
                count_col += 1
            board.append(row)
        count_row += 1

    return board