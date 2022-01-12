# o tabluleiro do nosso jogo vai ficar neste ficheiro, junto com as funções 
# para aceder, alterar este tabuleiro (esta mensagem vai ser removida 
# antes de submeter o projeto)


def new_board_instance(player_1_name=None, player_2_name=None, level=None):
    board = {
        'player_1': {
            'name': player_1_name,
            'pockets': [4, 4, 4, 4, 4, 4, 0]
        },
        'player_2': {
            'name': player_2_name,
            'pockets': [4, 4, 4, 4, 4, 4, 0]
        },
        'level': level 
    } 
    return board


def set(board, new_board):
    board = new_board


def update(board, 
        player_1_name=None, 
        player_2_name=None,  
        level=None,
        pockets_1=[4, 4, 4, 4, 4, 4, 0], 
        pockets_2=[4, 4, 4, 4, 4, 4, 0]):

    board['player_1']['name'] = player_1_name
    board['player_2']['name'] = player_2_name
    board['player_1']['pockets'] = pockets_1
    board['player_2']['pockets'] = pockets_2
    board['level'] = level
