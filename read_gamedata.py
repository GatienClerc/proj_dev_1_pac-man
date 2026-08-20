file_path = "gamedata/board.txt"

def read_gamedata(path):
    board = []

    with open(path, "r") as f:
        for line in f:
            row = []
            for char in line.rstrip("\n"):
                row.append(char)
            board.append(row)

    return board