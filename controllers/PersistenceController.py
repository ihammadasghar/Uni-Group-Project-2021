# toda a logíca relacionado com gravar/ler o estado de programa 
# vai ser implementado neste ficheiro (esta mensagem vai ser 
# removida antes de submeter o projeto)

import os
from controllers.GameController import create_player_instance
from models import Board
from models import PlayerRecord as PR


def load_game(filename):
    filepath = f"./saved/{filename}"
    if os.path.exists(filepath):
        with open(filepath, "r", encoding="utf-8") as file:
            lines = file.readlines()
            loaded_player_records = []
            loaded_board = {}
            checking_player_records = True
            for line in lines:
                if line != "\n":
                    if checking_player_records:
                        player = line[:-1].split(";")
                        instance = create_player_instance(*player)
                        loaded_player_records.append(instance)

                    else:
                        item = line.split(";")
                        name = item[0]
                        pockets = item[1][:-1].split(",")
                        pockets = [int(p) for p in pockets]
                        loaded_board[name] = pockets

                else:
                    checking_player_records = False

            Board.set(loaded_board)
            PR.set(loaded_player_records)
            print('loaded board', loaded_board)
            print('loader_player_records', loaded_player_records)
            return True
    else:
        return False

      
def save_game(filename):
    filepath = f"./saved/{filename}"
    with open(filepath, mode="w") as file:
        #  Save player records
        player_records = PR.all()
        for player in player_records:
            file.write(";".join([str(val) for val in player.values()]))
            file.write("\n")

        file.write("\n")

        #  Save board state
        board = Board.get()
        for name, pockets in board.items():
            line = name + ";" 
            line += ",".join([str(p) for p in pockets]) + "\n"
            file.write(line)
