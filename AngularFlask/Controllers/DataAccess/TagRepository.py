from Repository import Repository

class TagRepository(Repository):
	def __init__(self, connection_string):
		super(TagRepository, self).__init__(connection_string)

	def AddTag(self, tag_name, tag_type):
		command = """
		INSERT INTO BOARDGAME_TAGS(TAG_NAME, TAG_TYPE)
		VALUES ('{0}', '{1}')
		""".format(tag_name, tag_type)

		super(TagRepository, self).ExecuteCommand(command)

	def GetTags(self):
		command = "SELECT rowid, TAG_NAME, TAG_TYPE FROM BOARDGAME_TAGS"
		return super(TagRepository, self).GetQueryResults(command)

	def DeleteTags(self, tag_ids):
		command = "DELETE FROM BOARDGAME_TAGS WHERE ROWID IN ({0})".format(','.join(str(id) for id in tag_ids))
		super(TagRepository, self).ExecuteCommand(command)

		#CLEAN JT

if __name__ == '__main__':
	import os
	print "Testing"
	print os.path.join(os.getcwd(), '..', '..', '..', 'boardgames.db')
	tr = TagRepository(os.path.join(os.getcwd(), '..', '..', '..', 'boardgames.db'))
	tr.AddTag('Test', 'Tag')
	tr.AddTag('Another', 'Tag')
	r = tr.GetTags()
	print r
	tagids = [a["rowid"] for a in r]
	tr.DeleteTags(list(tagids))
	