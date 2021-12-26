# toda a logíca relacionado com gravar/ler o estado de programa 
# vai ser implementado neste ficheiro (esta mensagem vai ser 
# removida antes de submeter o projeto)

from models import Board
from models import PlayerRecord as PR

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
