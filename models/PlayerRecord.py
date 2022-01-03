# este ficheiro vai ter o registos de jogadores, junto com as funções 
# para aceder, adicionar novos registos e mais (esta mensagem vai ser removida 
# antes de submeter o projeto)

# Ex. player_records =  [{'name': 'Anees', 'played': 4, 'won': 2, 'drawn': 1, 'lost': 1}]

player_records = [
	{'name': 'CPU', 'played': 0, 'won': 0, 'drawn': 0, 'lost': 0}
]


def all():
	return player_records


def create(new_player_record):
	player_records.append(new_player_record)


def set(new_player_records):
	global player_records
	player_records = new_player_records


def get_player(player_name):
	for player in player_records:
		if player['name'] == player_name:
			return player
