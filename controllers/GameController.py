from models import Board, PlayerRecord


def get_game_data():
	# return game_data with 2 keys - 'board' and 'player_records'
	game_data = {
		'player_records': [PlayerRecord.new_player_record("CPU")],
		'board': {
			'player_1': {
				'name': None,
				'pockets': None
			},
			'player_2': {
				'name': None,
				'pockets': None
			},
			'level': None 
		} 
	}
	return game_data


def register_player(player_records, player_name):
	# return false if a player with this name already exists
	for player in player_records:
		if player['name'] == player_name:
			return False

	# create and add player to player_records
	new_player_record = PlayerRecord.new_player_record(player_name)
	PlayerRecord.create(player_records, new_player_record)
	return True


def sort_players(players):
	n_players = len(players)
	sorted_players = players.copy()

	# bubble-sort sorting algorithm
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


def get_sorted_players(player_records):
	sorted_players = sort_players(player_records) # sort players by wins and then name
	return sorted_players


def is_game_in_progress(board):
	# a game is in progress if the player_1 name in the program's board is not None
	if board['player_1']['name']:
		return True
	return False


def start_game(player_records, board, player_1_name, player_2_name, level=None):
	result = {'game_in_progress': False, 'player_not_found': False}

	# check if no game is already in progress
	if is_game_in_progress(board):
		result['game_in_progress'] = True 
		return result

	player_1 = PlayerRecord.get_player(player_records, player_1_name)
	player_2 = PlayerRecord.get_player(player_records, player_2_name)

	# check if players are registered
	if player_1 is None or player_2 is None:
		result['player_not_found'] = True
		return result 

	# update board for the game
	Board.update(board, 
		player_1_name=player_1_name,
		player_2_name=player_2_name,
		player_1_pockets=[4, 4, 4, 4, 4, 4, 0],
		player_2_pockets=[4, 4, 4, 4, 4, 4, 0],
		level=level
	)

	# update player records
	PlayerRecord.update(player_1, {'played': player_1['played']+1})
	PlayerRecord.update(player_2, {'played': player_2['played']+1})

	return result 


def is_part_of_game(board, player_name):
	# check if player with the given name is part of the present game
	if (board['player_1']['name'] == player_name) or board['player_2']['name'] == player_name:
		return True
	return False


def player_move(player_records, board, player_name, pos):
	pos -= 1 # convert pos provided by user to zero-based
	
	# dict to be returned
	result = {
		'no_game_in_progress': False, 
		'player_not_found': False, 
		'player_not_in_game': False, 
		'game_over_data': {}, 
		'has_another_move': False
	}

	# check if a game is in progress
	if not is_game_in_progress(board):
		result['no_game_in_progress'] = True
		return result

	player = PlayerRecord.get_player(player_records, player_name)
		
	# check if player is registered
	if player is None:
		result['player_not_found'] = True
		return result

	# check if player is part of the current game
	if not is_part_of_game(board, player_name): 
		result['player_not_in_game'] = True
		return result 
	
	# execute player move
	has_another_move = execute_move(board, pos, player_name)

	# check if either player has no more seeds left to play
	if is_game_over(board):
		result['game_over_data'] = wrap_up_game(board, player_records) # returns game_over_data
		return result

	# check if player has right to another move
	if has_another_move:
		result['has_another_move'] = True
		return result

	# make CPU move if playing against CPU
	if board['player_2']['name'] == 'CPU':
		while True:
			pos = find_auto_move(board) # find a move for the CPU
			has_another_move = execute_move(board, pos, player_name='CPU')
			
			# check if either player has no seeds left to play
			if is_game_over(board):
				result['game_over_data'] = wrap_up_game(board, player_records)
				return result
			
			# break the loop if auto player does not have a right to another move
			if not has_another_move: break
	
	return result


def execute_move(board, pos, player_name):
	has_another_move = False # return value

	# initialize all_pockets as a list of pockets of player who's making the move + the
	# pockets of the opponent (helps in implementing the 'spread seeds' logic)
	if board['player_1']['name'] == player_name:
		all_pockets = board['player_1']['pockets'] + board['player_2']['pockets']
	else:
		all_pockets = board['player_2']['pockets'] + board['player_1']['pockets']

	#  spread seeds
	seeds_to_spread = all_pockets[pos]
	all_pockets[pos] = 0 # remove seeds from the selected position
	while seeds_to_spread:
		pos = (pos + 1) % 13
		all_pockets[pos] += 1
		seeds_to_spread -= 1

	#  if last seed was placed in the player's own base, player has another move
	if pos == 6: has_another_move = True

	#  capture if player has right to capture
	elif (pos < 6) and (all_pockets[pos] == 1):
		opposite_pocket_seeds = all_pockets[12-pos]
		if opposite_pocket_seeds:
			all_pockets[12-pos] = 0
			all_pockets[pos] = 0
			all_pockets[6] += opposite_pocket_seeds + 1

	# update the players' pockets in board
	if board['player_1']['name'] == player_name: # if player_1 is making this move
		Board.update(board, player_1_pockets=all_pockets[:7], player_2_pockets=all_pockets[7:])
	else: # if player_2 is making this move
		Board.update(board, player_1_pockets=all_pockets[7:], player_2_pockets=all_pockets[:7])
		
	return has_another_move


def is_game_over(board):
	# return true if either player has no more seeds left to play
	if sum(board["player_1"]["pockets"][:6]) == 0 or sum(board["player_2"]["pockets"][:6]) == 0:
		return True 
	return False 


def wrap_up_game(board, player_records):
	# dict to be returned
	game_over_data = {
		'player_1_name': board['player_1']['name'],
		'player_2_name': board['player_2']['name'],
		'player_1_seeds': sum(board['player_1']['pockets']),
		'player_2_seeds': sum(board['player_2']['pockets']),
	}

	# update player records
	player_1 = PlayerRecord.get_player(player_records, board['player_1']['name'])
	player_2 = PlayerRecord.get_player(player_records, board['player_2']['name'])

	if game_over_data['player_1_seeds'] > game_over_data['player_2_seeds']: # player 1 won
		PlayerRecord.update(player_1, {'won': player_1['won']+1})
		PlayerRecord.update(player_2, {'lost': player_2['lost']+1})
	
	elif game_over_data['player_1_seeds'] < game_over_data['player_2_seeds']: # player 2 won
		PlayerRecord.update(player_1, {'lost': player_1['lost']+1})
		PlayerRecord.update(player_2, {'won': player_2['won']+1})

	else: # game ended in a draw
		PlayerRecord.update(player_1, {'draw': player_1['draw']+1})
		PlayerRecord.update(player_2, {'draw': player_2['draw']+1})

	# reset the board
	Board.reset(board)

	return game_over_data


def find_auto_move(board):
	cpu_pockets = board['player_2']['pockets']

	if board['level'] == 'Normal': # normal game difficulty
		# return the left-most available move
		for i in range(6):
			if cpu_pockets[i]: return i

	else: # advanced game difficulty
		# return the move that lets the CPU capture
		for i in range(6): 
			last_pos = i + cpu_pockets[i] # the position where the last seed would be dropped

			# i < last_pos < 6 - the last_pos is one of the pockets of the CPU (except base)
			# cpu_pockets[last_pos] == 0 - the pocket with position last_pos has no seeds
			# board['player_1']['pockets'][5-last_pos] != 0 - the pocket in front of last_pos has seeds available
			if (i < last_pos < 6) and (cpu_pockets[last_pos] == 0) and \
				(board['player_1']['pockets'][5-last_pos] != 0):
				return i
		
		# return the move that ends in the base
		for i in range(6):
			last_pos = i + cpu_pockets[i] # the position where the last seed would be dropped
			if last_pos == 6: return i

		# return the right-most available move
		for i in range(5, -1, -1):
			if cpu_pockets[i]: return i


def give_up_game(player_records, board, player_names):
	result = {'no_game_in_progress': False, 'player_not_found': False, 'player_not_in_game': False}

	# check if a game is in progress
	if not is_game_in_progress(board):
		result['no_game_in_progress'] = True
		return result

	if len(player_names) == 1: # if 1 player gave up
		player = PlayerRecord.get_player(player_records, player_names[0])
		
		# check if player is registered
		if player is None:
			result['player_not_found'] = True
			return result 

		# check if player is part of the current game
		if not is_part_of_game(board, player['name']): 
			result['player_not_in_game'] = True
			return result 
		
		# get the other player
		if board['player_1']['name'] == player['name']:
			other_player = PlayerRecord.get_player(player_records, board['player_2']['name'])
		else:
			other_player = PlayerRecord.get_player(player_records, board['player_1']['name'])

		# update player records
		PlayerRecord.update(player, {'lost': player['lost']+1})
		PlayerRecord.update(other_player, {'won': other_player['won']+1})

	elif len(player_names) == 2: # if 2 players gave up
		player_1 = PlayerRecord.get_player(player_records, player_names[0])
		player_2 = PlayerRecord.get_player(player_records, player_names[1])

		# check if both players are registered
		if player_1 is None or player_2 is None:
			result['player_not_found'] = True
			return result

		# check if both players are part of the current game
		if not is_part_of_game(board, player_1['name']) or not is_part_of_game(board, player_2['name']):
			result['player_not_in_game'] = True
			return result

		# update player records
		PlayerRecord.update(player_1, {'lost': player_1['lost']+1})
		PlayerRecord.update(player_2, {'lost': player_2['lost']+1})

	# reset board
	Board.reset(board)

	return result
