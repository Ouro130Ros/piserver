from Repository import Repository

class PlayerRepository(Repository):
	def __init__(self, connection_string):
		super(PlayerRepository, self).__init__(connection_string)

	def AddPlayer(self, first_name, last_name):
		command = "INSERT INTO BOARDGAME_PLAYER (PLAYER_FIRST_NAME, PLAYER_LAST_NAME) VALUES ('{0}', '{1}')".format(first_name, last_name)
		super(PlayerRepository, self).ExecuteCommand(command)

	def GetPlayers(self):
		query = "SELECT rowid, PLAYER_FIRST_NAME, PLAYER_LAST_NAME FROM BOARDGAME_PLAYER"
		return super(PlayerRepository, self).GetQueryResults(query)

	def DeletePlayers(self, player_ids):
		command = "DELETE FROM BOARDGAME_PLAYER WHERE ROWID IN ({0})".format(','.join(str(id) for id in player_ids))
		super(PlayerRepository, self).ExecuteCommand(command)

if __name__ == "__main__":
	import os
	print "Testing"
	path = os.path.join(os.getcwd(), '..', '..', '..', 'boardgames.db')
	pr = PlayerRepository(path)
	pr.AddPlayer('Joe', 'Schmoo')
	r = pr.GetPlayers()
	print r
	pr.DeletePlayers([a['rowid'] for a in r])
