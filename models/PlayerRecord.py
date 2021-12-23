# este ficheiro vai ter o registos de jogadores, junto com as funções 
# para aceder, adicionar novos registos e mais (esta mensagem vai ser removida 
# antes de submeter o projeto)

# Ex. player_records = [{'name': Anees, 'played': 4, 'won', 2, 'drawn': 1, 'lost': 1}]

player_records = []


def all():
	return player_records


def create(new_player_record):
	player_records.append(new_player_record)
	return