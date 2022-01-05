# toda a lógica relacionada com a interacção com o utilizador vai ser 
# implementado neste ficheiro (esta mensagem vai ser removida antes 
# de submeter o projeto)

from controllers import GameController as gclr
from controllers import PersistenceController as pclr


def main():
	while True:
		user_input = input()
		commands = user_input.split(' ')
		command = commands[0].upper()

		if command == 'RJ':
			if is_arguments_length(commands, 1):
				register_player(player_name=commands[1])

		elif commands == 'LJ':
			if len(commands)-1 != 0:
				print('Instrução inválida.')
				continue
			list_players()

		elif command == 'IJ':
			if is_arguments_length(commands, 2):
				start_game(player_1_name=commands[1], player_2_name=commands[2])

		elif command == 'IJA':
			if is_arguments_length(commands, 2):
				start_auto_game(player_name=commands[1], level=commands[2])

		elif command == 'L':
			if is_arguments_length(commands, 1): 
				load_game(filename=commands[1])
      
		elif command == 'G':
			if is_arguments_length(commands, 1):
				save_game(filename=commands[1])

		elif command == 'DJ':
			if is_arguments_length(commands, 0):
				display_game_detail()
		
		elif command == 'D':
			if is_arguments_length(commands, 1) or is_arguments_length(commands, 2):
				give_up_game(commands[1:])
        
		# close the program, if a blank line is entered
		elif command == '':
			break

		else:
			print('Instrução inválida.')


def register_player(player_name):
	registered = gclr.register_player(player_name)

	if registered:
		print("Jogador registado com sucesso.")
	else:
		print("Jogador existente.")

def list_players():
	players = gclr.get_players()

	for player in players:
		print("{} {} {} {} {}".format(*player.values()))

def load_game(filename):
	loaded = pclr.load_game(filename)

	if loaded:
		print("Jogo lido com sucesso.")
	else:
		print("Ficheiro inexistente.")


def save_game(filename):
	pclr.save_game(filename)
	print("Jogo gravado com sucesso.")


def start_game(player_1_name, player_2_name):
	result = gclr.start_game(player_1_name, player_2_name)

	if result['game_in_progress']:
		print('Existe um jogo em curso.')
	elif result['player_not_found']:
		print('Jogador inexistente.')
	else:
		print(f'Jogo iniciado com sucesso.')


def start_auto_game(player_name, level):
	result = gclr.start_game(player_name, 'CPU', level)

	if result['game_in_progress']:
		print('Existe um jogo em curso.')
	elif result['player_not_found']:
		print('Jogador inexistente.')
	else:
		print(f'Jogo automático de nivel {level} iniciado com sucesso.')


def display_game_detail():
	board = gclr.get_game_detail()
	players = [board['player_1'], board['player_2']]
	for player in players:
		print("{} ({}) ({}) ({}) ({}) ({}) ({}) [{}]".format(player['name'], *player['pockets']))


def give_up_game(player_names):
	result = gclr.give_up_game(player_names)

	if result['no_game_in_progress']:
		print('Não existe jogo em curso.')
	elif result['player_not_found']:
		print('Jogador inexistente.')
	elif result['player_not_in_game']:
		print('Jogador não participa no jogo em curso.')
	else:
		print('Jogo terminado com sucesso.')
		
    
def is_arguments_length(commands, length):
	if len(commands)-1 != length:  
		print('Instrução inválida.')
		return False
	return True
