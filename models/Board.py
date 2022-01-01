# o tabluleiro do nosso jogo vai ficar neste ficheiro, junto com as funções 
# para aceder, alterar este tabuleiro (esta mensagem vai ser removida 
# antes de submeter o projeto)

board = {
    'player_1': {
        'name': None,
        'pockets': [0, 0, 0, 0, 0, 0, 0]
    },
    'player_2': {
        'name': None,
        'pockets': [0, 0, 0, 0, 0, 0, 0]
    },
    'level': None
}


def get():
    return board


def set(new_board):
    global board
    board = new_board
