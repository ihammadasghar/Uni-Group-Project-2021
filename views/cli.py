# toda a lógica relacionada com a interacção com o utilizador vai ser 
# implementado neste ficheiro (esta mensagem vai ser removida antes 
# de submeter o projeto)

from controllers import GameController as gclr
from controllers import PersistenceController as pclr


def main():
	game_data = gclr.get_game_data()

	while True:
		user_input = input()
		commands = user_input.split(' ')
		command = commands[0].upper()

		if command == 'RJ':
			if len(commands)-1 != 1:
				print('Instrução inválida.')
				continue
			register_player(game_data['player_records'], player_name=commands[1])

		elif command == 'LJ':
			if len(commands)-1 != 0:
				print('Instrução inválida.')
				continue
			list_players(game_data['player_records'])

		elif command == 'IJ':
			if len(commands)-1 != 2:
				print('Instrução inválida.')
				continue
			start_game(game_data['player_records'], game_data['board'], player_1_name=commands[1], player_2_name=commands[2])

		elif command == 'IJA':
			if len(commands)-1 != 2:
				print('Instrução inválida.')
				continue
			start_auto_game(game_data['player_records'], game_data['board'], player_name=commands[1], level=commands[2])

		elif command == 'L':
			if len(commands)-1 != 1:
				print('Instrução inválida.')
				continue
			game_data = load_game(filename=commands[1])
      
		elif command == 'G':
			if len(commands)-1 != 1:
				print('Instrução inválida.')
				continue
			save_game(game_data, filename=commands[1])

		elif command == 'DJ':
			if len(commands)-1 != 0:
				print('Instrução inválida.')
				continue
			display_game_detail(game_data['board'])
		
		elif command == 'D':
			if len(commands)-1 not in [1, 2]:
				print('Instrução inválida.')
				continue
			give_up_game(game_data['player_records'], game_data['board'], player_names=commands[1:])

		elif command == 'J':
			if len(commands)-1 != 2:
				print('Instrução inválida.')
				continue
			player_move(game_data['player_records'], game_data['board'], player_name=commands[1], pos=commands[2])

		# close the program, if a blank line is entered
		elif command == '':
			break

		else:
			print('Instrução inválida.')


def register_player(player_records, player_name):
	is_registered = gclr.register_player(player_records, player_name)

	if is_registered:
		print("Jogador registado com sucesso.")
	else:
		print("Jogador existente.")


def list_players(player_records):
	players = gclr.get_sorted_players(player_records)

	for player in players:
		print("{} {} {} {} {}".format(*player.values()))


def load_game(filename):
	data = pclr.load_game(filename)

	if data:
		print("Jogo lido com sucesso.")
		return data
	else:
		print("Ficheiro inexistente.")


def save_game(game_data, filename):
	pclr.save_game(game_data, filename)
	print("Jogo gravado com sucesso.")


def start_game(player_records, board, player_1_name, player_2_name):
	result = gclr.start_game(player_records, board, player_1_name, player_2_name)

	if result['game_in_progress']:
		print('Existe um jogo em curso.')
	elif result['player_not_found']:
		print('Jogador inexistente.')
	else:
		print(f'Jogo iniciado com sucesso.')


def start_auto_game(player_records, board, player_name, level):
	result = gclr.start_game(player_records, board, player_name, 'CPU', level)

	if result['game_in_progress']:
		print('Existe um jogo em curso.')
	elif result['player_not_found']:
		print('Jogador inexistente.')
	else:
		print(f'Jogo automático de nivel {level} iniciado com sucesso.')


def display_game_detail(board):
	if not gclr.game_in_progress(board):
		print("Não existe jogo em curso.")
		return

	players = [board['player_1'], board['player_2']]
	for player in players:
		print("{} ({}) ({}) ({}) ({}) ({}) ({}) [{}]".format(player['name'], *player['pockets']))


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
		print('Jogo terminado.')
		print(f'{player_1_name} {player_1_seeds}')
		print(f'{player_2_name} {player_2_seeds}')
	elif result['has_another_move']:
		print(f'O jogador {player_name} tem direito a outra jogada.')
	else:
		print('Jogo terminado com sucesso.')
