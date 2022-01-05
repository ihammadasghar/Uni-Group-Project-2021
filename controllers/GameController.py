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


def sort_players(players): # bubble sort algorithm
	n_players = len(players)
	sorted_players = players.copy()

	for i in range(n_players):
		for j in range(n_players-i-1):
			# case 1 - the player j has won less games than player j+1
			case_1 = sorted_players[j]['won'] < sorted_players[j+1]['won']

			# case 2 - player j and j+1 have equal number of wins but player j's
			# name is lower alphabetically than player j+1
			case_2 = (sorted_players[j]['won'] == sorted_players[j+1]['won']) \
					and (sorted_players[j]['name'] > sorted_players[j+1]['name'])

			if case_1 or case_2:
				tmp = sorted_players[j]
				sorted_players[j] = sorted_players[j+1]
				sorted_players[j+1] = tmp

	return sorted_players


def get_players():
	players = PlayerRecord.all()
	sorted_players = sort_players(players) # sort players by wins and then name
	return sorted_players


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
	if not game_in_progress(): # return none if no game in progress
		return

	board = Board.get()
	return board


def give_up_game(player_names):
	result = {'no_game_in_progress': False, 'player_not_found': False, 'player_not_in_game': False}

	# check if a game is in progress
	if not game_in_progress():
		result['no_game_in_progress'] = True
		return result

	board = Board.get()

	if len(player_names) == 1: # if one player gaver up
		player = PlayerRecord.get_player(player_names[0])
		
		# check if player is registered
		if player is None:
			result['player_not_found'] = True
			return result 

		# check if player is part of the current game
		if player['name'] not in [board['player_1']['name'], board['player_2']['name']]: 
			result['player_not_in_game'] = True
			return result 
		
		# get the other player
		if board['player_1']['name'] == player['name']:
			other_player = PlayerRecord.get_player(board['player_2']['name'])
		else:
			other_player = PlayerRecord.get_player(board['player_1']['name'])

		# update player records
		player['lost'] += 1
		other_player['won'] += 1 

	elif len(player_names) == 2: # if 2 players gave up
		player_1 = PlayerRecord.get_player(player_names[0])
		player_2 = PlayerRecord.get_player(player_names[1])

		# check if both players are registered
		if player_1 is None or player_2 is None:
			result['player_not_found'] = True
			return result

		# check if both players are part of the current game
		board_players = [board['player_1']['name'], board['player_2']['name']]
		if player_1['name'] not in board_players or player_2['name'] not in board_players:
			result['player_not_in_game'] = True
			return result

		# update player records
		player_1['lost'] += 1
		player_2['lost'] += 1

	# reset board
	empty_board = new_board_instance()
	Board.set(empty_board)

	return result
