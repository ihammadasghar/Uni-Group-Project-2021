# toda a logíca relacionado com gravar/ler o estado de programa 
# vai ser implementado neste ficheiro (esta mensagem vai ser 
# removida antes de submeter o projeto)

from models import Board
from models import PlayerRecord as PR

def save_game(filename):
    FILEPATH = f"{filename}"
    with open(FILEPATH, mode="w") as file:
        #  Save player records
        player_records = PR.all()
        for player in player_records:
            file.write(";".join([str(val) for val in player.values()]))
            file.write(";\n")

        file.write("\n")

        #  Save board state
        board = Board.board
        for player in board.items():
            name = player[0]
            pockets = player[1]
            line = name + ";" 
            for i in range(len(pockets)): 
                if i != len(pockets)-1:  #  We dont want to include comma after the last element
                    line += str(pockets[i]) + ","
                else:
                    line += str(pockets[i]) + ";\n"
            
            file.write(line)
