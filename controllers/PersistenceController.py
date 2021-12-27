# toda a logíca relacionado com gravar/ler o estado de programa 
# vai ser implementado neste ficheiro (esta mensagem vai ser 
# removida antes de submeter o projeto)

import os
from models import Board
from models import PlayerRecord as PR
from controllers.GameController import create_player_instance


def load_game(filename):
    filepath = f"./saved/{filename}"

    # return false if file doesn't exist
    if not os.path.isfile(filepath):
        return False

    with open(filepath, "r", encoding="utf-8") as file:
        lines = file.readlines()

        # variables to fill from the opened file
        loaded_player_records = []
        loaded_board = {}

        checking_player_records = True

        for line in lines:
            if line == "\n":
                checking_player_records = False
                continue

            if checking_player_records:
                player = line[:-1].split(";")
                instance = create_player_instance(*player)
                loaded_player_records.append(instance)

            else:
                item = line.split(";")
                name, pockets = item[0], item[1][:-1].split(",")
                pockets = [int(p) for p in pockets]
                loaded_board[name] = pockets

        # update the board and player records of the program
        Board.set(loaded_board)
        PR.set(loaded_player_records)

        return True

    
def save_game(filename):
    # create "saved" directory if it doesn't exist already
    if not os.path.isdir('./saved'):
        os.mkdir('./saved')

    filepath = f"./saved/{filename}"

    with open(filepath, mode="w") as file:
        #  save player records
        player_records = PR.all()
        for player in player_records:
            file.write(";".join([str(val) for val in player.values()]))
            file.write("\n")

        file.write("\n")

        #  save board state
        board = Board.get()
        for name, pockets in board.items():
            line = name + ";" 
            line += ",".join([str(p) for p in pockets]) + "\n"
            file.write(line)
