# toda a logíca relacionado com gravar/ler o estado de programa 
# vai ser implementado neste ficheiro (esta mensagem vai ser 
# removida antes de submeter o projeto)

from models import Board
from models import PlayerRecord as PR


def load_game(filename):
    try:
        with open(filename, "r", encoding="utf-8") as file:
            lines = file.readlines()
            loaded_player_records = []
            loaded_board = {}
            checking = "records"
            for line in lines:
                if line != "\n":
                    if checking == "records":
                        player = line.split(";")

                        for i in range(len(player)):
                            try:
                                player[i] = int(player[i])
                            except ValueError:
                                pass

                        new_records.append({"name": player[0],"played": player[1],"won": player[2],"drawn": player[3],"lost": player[4]})

                    else:
                        item = line.split(";")
                        name = item[0]
                        pockets = item[1].split(",")
                        for i in range(len(pockets)):
                            pockets[i] = int(pockets[i])
                        new_board.update({name: pockets})

                else:
                    checking = "board"

            Board.board = new_board
            PR.player_records = new_records
            return True
            
    except FileNotFoundError:
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