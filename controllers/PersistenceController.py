# toda a logíca relacionado com gravar/ler o estado de programa 
# vai ser implementado neste ficheiro (esta mensagem vai ser 
# removida antes de submeter o projeto)

import os
import json
from models import Board
from models import PlayerRecord as PR


def load_game(filename):
    filepath = f"./saved/{filename}"

    # return false if file doesn't exist
    if not os.path.isfile(filepath):
        return False

    with open(filepath, "r", encoding="utf-8") as file:
        return json.load(file)

    
def save_game(game_data, filename):
    # create "saved" directory if it doesn't exist already
    if not os.path.isdir('./saved'):
        os.mkdir('./saved')

    filepath = f"./saved/{filename}"

    with open(filepath, mode="w") as file:
        json.dump(game_data, file)
