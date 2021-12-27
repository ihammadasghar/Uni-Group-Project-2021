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
			if len(commands) - 1 != 1:  
				print('Instrução inválida.')
				continue

			player_name = commands[1]
			register_player(player_name)

		elif command == 'L':
			if len(commands) - 1 != 1:  
				print('Instrução inválida.')
				continue
			filename = commands[1]
			load_game(filename)
      
		elif command == 'G':
			if len(commands) - 1 != 1:  
				print('Instrução inválida.')
				continue
			filename = commands[1]
			save_game(filename)

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


def load_game(filename):
	loaded = pclr.load_game(filename)

	if loaded:
		print("Jogo lido com sucesso.")
	else:
		print("Ficheiro inexistente.")
    

def save_game(filename):
	pclr.save_game(filename)
	print("Jogo gravado com sucesso.")
