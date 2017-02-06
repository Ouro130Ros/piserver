from Repository import Repository

class GameRepository(Repository):
	def __init__(self, connection_string):
		super(GameRepository, self).__init__(connection_string)

	def AddGame(self, title):
		command = "INSERT INTO BOARDGAME (TITLE) VALUES ('{0}')".format(title)
		super(GameRepository, self).ExecuteCommand(command)

	def _GenerateUpdateList(self, game_object):
		keys = [k for k in game_object.keys() if k.upper() != 'ROWID']
		updateStmt = "  {0} = {1}\n".format(
			keys[0], str(game_object[keys[0]]) 
			if isinstance(game_object[keys[0]], (int, long)) 
			else "'{0}'".format(game_object[keys[0]])
		)

		for key in keys[1:]:
			updateStmt += " ,{0} = {1}\n".format(
				key, str(game_object[key]) 
				if isinstance(game_object[key], (int, long)) 
				else "'{0}'".format(game_object[key])
			)
		return updateStmt

	def UpdateGame(self, game_object):
		command = """
		UPDATE BOARDGAME SET
		{0}
		WHERE ROWID = {1}""".format(self._GenerateUpdateList(game_object), game_object['rowid'])

		super(GameRepository, self).ExecuteCommand(command)

	def DeleteGame(self, game_id):
		command = "DELETE FROM BOARDGAME WHERE ROWID = {0}".format(game_id)
		categoryDeleteCommand = "DELETE FROM JT_BOARDGAME_SCORE_CATEGORY WHERE BOARDGAME_ROWID = {0}".format(game_id)
		gameTagDeleteCommand = "DELETE FROM JT_BOARDGAME_TAG WHERE BOARDGAME_ROWID = {0}".format(game_id)

		super(GameRepository, self).ExecuteCommand(categoryDeleteCommand)
		super(GameRepository, self).ExecuteCommand(gameTagDeleteCommand)
		super(GameRepository, self).ExecuteCommand(command)


	def GetAllGames(self):
		query = "SELECT rowid, TITLE, DESCRIPTION, MIN_PLAYERS, MAX_PLAYERS, IMAGE_PATH FROM BOARDGAME"
		return super(GameRepository, self).GetQueryResults(query)		

	def GetGame(self, game_id):
		query = "SELECT rowid, TITLE, DESCRIPTION, MIN_PLAYERS, MAX_PLAYERS, IMAGE_PATH FROM BOARDGAME WHERE ROWID = {0}".format(game_id) 
		results =  super(GameRepository, self).GetQueryResults(query)		
		if len(results) == 0: return None
		return results[0]

	def SetGameTags(self, game_id, tag_ids):
		deleteCommand = "DELETE FROM JT_BOARDGAME_TAG WHERE BOARDGAME_ROWID = {0}".format(game_id)
		super(GameRepository, self).ExecuteCommand(deleteCommand)

		valuesList = "  ({0},{1})".format(tag_ids[0], game_id)
		for tid in tag_ids[1:]:
			valuesList += " ,({0},{1})".format(tid, game_id)

		command = "INSERT INTO JT_BOARDGAME_TAG (TAG_ROWID, BOARDGAME_ROWID) VALUES {0}".format(valuesList)
		super(GameRepository, self).ExecuteCommand(command)

	def SetGameScoringCategory(self, game_id, category_ids):
		deleteCommand = "DELETE FROM JT_BOARDGAME_SCORE_CATEGORY WHERE BOARDGAME_ROWID = {0}".format(game_id)
		super(GameRepository, self).ExecuteCommand(deleteCommand)

		valuesList = "  ({0},{1})".format(category_ids[0], game_id)
		for tid in category_ids[1:]:
			valuesList += " ,({0},{1})".format(tid, game_id)

		command = "INSERT INTO JT_BOARDGAME_SCORE_CATEGORY (CATEGORY_ROWID, BOARDGAME_ROWID) VALUES {0}".format(valuesList)
		super(GameRepository, self).ExecuteCommand(command)

	def GetTagsForGame(self, game_id):
		query = """
		SELECT A.TAG_NAME, A.TAG_TYPE, A.rowid 
		FROM JT_BOARDGAME_TAG J 
		JOIN BOARDGAME_TAGS A ON J.TAG_ROWID = A.ROWID 
		WHERE J.BOARDGAME_ROWID = {0}""".format(game_id)

		return super(GameRepository, self).GetQueryResults(query)

	def GetCategoriesForGame(self, game_id):
		query = """
		SELECT A.CATEGORY_NAME, A.CATEGORY_TYPE, A.rowid 
		FROM JT_BOARDGAME_SCORE_CATEGORY J 
		JOIN BOARDGAME_SCORING_CATEGORY A ON J.CATEGORY_ROWID = A.ROWID 
		WHERE J.BOARDGAME_ROWID = {0}""".format(game_id)

		return super(GameRepository, self).GetQueryResults(query)

if __name__ == '__main__':
	import os
	from TagRepository import TagRepository
	print "Testing"
	path = os.path.join('boardgames.db')
	gr = GameRepository(path)
	tr = TagRepository(path)

	gr.AddGame("7 Wonders")
	games = gr.GetAllGames()
	print games

	tr.AddTag("Drafting", "MECHANIC")
	gr.SetGameTags(games[0]['rowid'], [1])

	games[0]["DESCRIPTION"] = "Pass Cards Around"
	games[0]["MIN_PLAYERS"] = 3
	games[0]["MAX_PLAYERS"] = 7
	gr.UpdateGame(games[0])
	games = gr.GetAllGames()
	print games

	print gr.GetTagsForGame(games[0]['rowid'])

	print gr.GetGame(games[0]['rowid'])

	gr.DeleteGame(games[0]['rowid'])

