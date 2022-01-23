from controllers import GameController as gclr
from controllers import PersistenceController as pclr


def main():
	game_data = gclr.get_game_data()

	while True:
		user_input = input()
		commands = user_input.split(' ')
		command = commands[0].upper()

		if command == 'RJ':
			if is_nargs_correct(commands, 1):
				register_player(game_data['player_records'], player_name=commands[1])

		elif command == 'LJ':
			if is_nargs_correct(commands, 0):
				list_players(game_data['player_records'])

		elif command == 'IJ':
			if is_nargs_correct(commands, 2):
				start_game(game_data['player_records'], game_data['board'], \
					player_1_name=commands[1], player_2_name=commands[2])

		elif command == 'IJA':
			if is_nargs_correct(commands, 2):
				start_auto_game(game_data['player_records'], game_data['board'], \
					player_name=commands[1], level=commands[2])

		elif command == 'L':
			if is_nargs_correct(commands, 1):
				game_data = pclr.load_game(filename=commands[1])
				print("Jogo lido com sucesso.")
      
		elif command == 'G':
			if is_nargs_correct(commands, 1):
				pclr.save_game(game_data, filename=commands[1])
				print("Jogo gravado com sucesso.")

		elif command == 'DJ':
			if is_nargs_correct(commands, 0):
				display_game_detail(game_data['board'])
		
		elif command == 'D':
			if is_nargs_correct(commands, [1, 2]):
				give_up_game(game_data['player_records'], game_data['board'], player_names=commands[1:])

		elif command == 'J':
			if is_nargs_correct(commands, 2):
				player_move(game_data['player_records'], game_data['board'], \
					player_name=commands[1], pos=int(commands[2]))

		# close the program, if a blank line is entered
		elif command == '': break

		else: print('Instrução inválida.')


def is_nargs_correct(commands, correct_vals):
	"""
		Checks if number of arguments passed by user is correct.
	"""
	if type(correct_vals) is not list:
		correct_vals = [correct_vals]
	
	if len(commands)-1 not in correct_vals: # -1 as we dont count the command as arg
		print("Instrução inválida.")
		return False
	return True


def register_player(player_records, player_name):
	success = gclr.register_player(player_records, player_name)

	if success:
		print("Jogador registado com sucesso.")
	else:
		print("Jogador existente.")


def list_players(player_records):
	players = gclr.get_sorted_players(player_records)

	for player in players:
		print("{} {} {} {} {}".format(*player.values()))


def start_game(player_records, board, player_1_name, player_2_name):
	result = gclr.start_game(player_records, board, player_1_name, player_2_name)

	if result['game_in_progress']:
		print('Existe um jogo em curso.')
	elif result['player_not_found']:
		print('Jogador inexistente.')
	else:
		print('Jogo iniciado com sucesso.')


def start_auto_game(player_records, board, player_name, level):
	result = gclr.start_game(player_records, board, \
		player_1_name=player_name, player_2_name='CPU', level=level)

	if result['game_in_progress']:
		print('Existe um jogo em curso.')
	elif result['player_not_found']:
		print('Jogador inexistente.')
	else:
		print(f'Jogo automático de nível {level} iniciado com sucesso.')


def display_game_detail(board):
	if not gclr.is_game_in_progress(board):
		print("Não existe jogo em curso.")
		return

	players = [board['player_1'], board['player_2']]
	for player in players:
		print("{} [{}] [{}] [{}] [{}] [{}] [{}] ({})".format(player['name'], *player['pockets']))


def give_up_game(player_records, board, player_names):
	result = gclr.give_up_game(player_records, board, player_names)

	if result['no_game_in_progress']:
		print('Não existe jogo em curso.')
	elif result['player_not_found']:
		print('Jogador inexistente.')
	elif result['player_not_in_game']:
		print('Jogador não participa no jogo em curso.')
	else:
		print('Jogo terminado com sucesso.')


def player_move(player_records, board, player_name, pos):
	result = gclr.player_move(player_records, board, player_name, pos)

	if result['no_game_in_progress']:
		print('Não existe jogo em curso.')

	elif result['player_not_found']:
		print('Jogador inexistente.')

	elif result['player_not_in_game']:
		print('Jogador não participa no jogo em curso.')

	elif result["game_over_data"]:
		game_over_data = result['game_over_data']
		print('Jogo terminado.')
		print(f"{game_over_data['player_1_name']} {game_over_data['player_1_seeds']}")
		print(f"{game_over_data['player_2_name']} {game_over_data['player_2_seeds']}")

	elif result['has_another_move']:
		print(f'O jogador {player_name} tem direito a outra jogada.')

	else:
		print('Jogada efetuada com sucesso.')
