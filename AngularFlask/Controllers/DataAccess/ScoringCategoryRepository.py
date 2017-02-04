from Repository import Repository

class ScoringCategoryRepository(Repository):
	def __init__(self, connection_string):
		super(ScoringCategoryRepository, self).__init__(connection_string)

	def AddCategory(self, category_name, category_type):
		command = """
		INSERT INTO BOARDGAME_SCORING_CATEGORY(TAG_NAME, TAG_TYPE)
		VALUES ('{0}', '{1}')
		""".format(category_name, category_type)

		super(AddCategory, self).ExecuteCommand(command)

	def GetCategory(self):
		command = "SELECT rowid, TAG_NAME, TAG_TYPE FROM BOARDGAME_SCORING_CATEGORY"
		return super(AddCategory, self).GetQueryResults(command)

	def DeleteCategory(self, tag_ids):
		command = "DELETE FROM BOARDGAME_SCORING_CATEGORY WHERE ROWID IN ({0})".format(','.join(str(id) for id in tag_ids))
		super(AddCategory, self).ExecuteCommand(command)