# toda a logíca relacionado com o jogo (criar jogadores, listar jogadores,
# efetuar jogada e mais) vai ser implementado neste ficheiro (esta mensagem 
# vai ser removida antes de submeter o projeto)

from models import Board
from models import PlayerRecord


def register_player(player_name):
	players = PlayerRecord.all()
	for p in players:
		# return false if player with this name already exists
		if p['name'] == player_name:
			return False

	# create and add player to player_records
	new_player_record = new_player_instance(player_name)
	PlayerRecord.create(new_player_record)
	return True


def new_player_instance(player_name):
	player = {
		'name': player_name, 'played': 0, 'won': 0, 'drawn': 0, 'lost': 0
	}
	return player


def bubble_sort(itens):
	pass


def get_players():
	players = PlayerRecord.all()
	bubble_sort(players)
	return players



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


def game_in_progress():
	board = Board.get()

	# if the player_1 name in the program's board is not None,
	# a game is in progress
	if board['player_1']['name']:
		return True
	else:
		return False


def start_game(player_1_name, player_2_name, level=None):
	result = {'game_in_progress': False, 'player_not_found': False}

	# check if no game is already in progress
	if game_in_progress():
		result['game_in_progress'] = True 
		return result

	player_1 = PlayerRecord.get_player(player_1_name)
	player_2 = PlayerRecord.get_player(player_2_name)

	# check if players are registered
	if player_1 is None or player_2 is None:
		result['player_not_found'] = True
		return result 

	# set up board for the game
	board = new_board_instance(player_1_name, player_2_name, level)
	Board.set(board) 

	# update player records
	player_1['played'] += 1
	player_2['played'] += 1

	return result 


def get_game_detail():
	board = Board.get()
	return board


def give_up_game(player_names):
	result = {'no_game_in_progress': False, 'player_not_found': False, 'player_not_in_game': False}

	if not game_in_progress():
		result['no_game_in_progress'] = True
		return result

	board = Board.get()

	if len(player_names) == 1:
		player = PlayerRecord.get_player(player_names[0])
		
		if player is None:
			result['player_not_found'] = True
			return result 

		if player['name'] not in [board['player_1']['name'], board['player_2']['name']]: 
			result['player_not_in_game'] = True
			return result 
		
		if board['player_1']['name'] == player['name']:
			other_player = PlayerRecord.get_player(board['player_2']['name'])
		else:
			other_player = PlayerRecord.get_player(board['player_1']['name'])

		player['lost'] += 1
		other_player['won'] += 1 

	elif len(player_names) == 2:
		player_1 = PlayerRecord.get_player(player_names[0])
		player_2 = PlayerRecord.get_player(player_names[1])

		if player_1 is None or player_2 is None:
			result['player_not_found'] = True
			return result

		board_players = [board['player_1']['name'], board['player_2']['name']]
		if player_1['name'] not in board_players or player_2['name'] not in board_players:
			result['player_not_in_game'] = True
			return result

		player_1['lost'] += 1
		player_2['lost'] += 1

	empty_board = new_board_instance()
	Board.set(empty_board)
	return result
