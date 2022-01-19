import os
import json


def load_game(filename):
    filepath = f"./saved/{filename}"

    with open(filepath, "r", encoding="utf-8") as file:
        return json.load(file)

    
def save_game(game_data, filename):
    # create "saved" directory if it doesn't exist already
    if not os.path.isdir('./saved'):
        os.mkdir('./saved')

    filepath = f"./saved/{filename}"

    with open(filepath, mode="w") as file:
        json.dump(game_data, file)
