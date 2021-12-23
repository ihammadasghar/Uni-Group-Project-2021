# toda a logíca relacionado com o jogo (criar jogadores, listar jogadores,
# efetuar jogada e mais) vai ser implementado neste ficheiro (esta mensagem 
# vai ser removida antes de submeter o projeto)

from models import Board
from models import PlayerRecord


def register_player(player_name):
	players = PlayerRecord.all()

	for p in players:
		if p['name'] == player_name:
			# já existe um jogador com este nome
			return False

	new_player_record = {
		'name': player_name,
		'played': 0,
		'won': 0,
		'drawn': 0,
		'lost': 0
	}

	PlayerRecord.create(new_player_record)
	return True
