# o tabluleiro do nosso jogo vai ficar neste ficheiro, junto com as funções 
# para aceder, alterar este tabuleiro (esta mensagem vai ser removida 
# antes de submeter o projeto)

def update(board, player_1_name=None, player_2_name=None, player_1_pockets=None, player_2_pockets=None, level=None):
    if player_1_name:
        board['player_1']['name'] = player_1_name
    if player_2_name:
        board['player_2']['name'] = player_2_name
    if player_1_pockets:
        board['player_1']['pockets'] = player_1_pockets
    if player_2_pockets:
        board['player_2']['pockets'] = player_2_pockets
    if level:
        board['level'] = level


def reset(board):
    board['player_1']['name'] = None
    board['player_2']['name'] = None
    board['player_1']['pockets'] = None
    board['player_2']['pockets'] = None
    board['level'] = None
