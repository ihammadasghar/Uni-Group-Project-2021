# este ficheiro vai ter o registos de jogadores, junto com as funções 
# para aceder, adicionar novos registos e mais (esta mensagem vai ser removida 
# antes de submeter o projeto)

# Ex. player_records =  [{'name': 'Anees', 'played': 4, 'won': 2, 'drawn': 1, 'lost': 1}]


def new_player_instance(player_name):
	player = {
		'name': player_name, 'played': 0, 'won': 0, 'drawn': 0, 'lost': 0
	}
	return player


def create(player_records, new_player_record):
	player_records.append(new_player_record)


def get_player(player_records, player_name):
	for player in player_records:
		if player['name'] == player_name:
			return player
