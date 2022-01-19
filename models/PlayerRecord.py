
def new_player_record(player_name):
	"""
		Given a player name, create and returns a new instance of player record with
		that name.
	"""
	player_record = {
		'name': player_name, 'played': 0, 'won': 0, 'drawn': 0, 'lost': 0
	}
	return player_record


def create(player_records, new_player_record):
	"""
		Add the new player record to the program's list of players.
	"""
	player_records.append(new_player_record)


def get_player(player_records, player_name):
	"""
		Search player records and return the player record with name equal to 
		the name passed as parameter.
	"""
	for player in player_records:
		if player['name'] == player_name:
			return player


def update(player, to_be_updated):
	"""
		Update player record with the new values passed as a dictionary (to_be_updated).
	"""
	for key, value in to_be_updated.items():
		player[key] = value
