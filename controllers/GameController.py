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
	new_player_record = create_player_instance(player_name)
	PlayerRecord.create(new_player_record)
	return True


def create_player_instance(player_name, played=0, won=0, drawn=0, lost=0):
	new_player_record = {
		'name': player_name,
		'played': int(played),
		'won': int(won),
		'drawn': int(drawn),
		'lost': int(lost)
	}
	return new_player_record


def game_in_progress():
	board = Board.get()

	if board['player_1']['name']:
		return True
	else:
		return False
