import sqlite3
from sqlite3 import OperationalError

def dict_factory(cursor, row):
    d = {}
    for idx,col in enumerate(cursor.description):
        d[col[0]] = row[idx]
    return d

class Repository(object):
	def __init__(self, database_path):
		self.ConnectionString = database_path
		
	def _GetConnection(self):
		connection = sqlite3.connect(self.ConnectionString)
		connection.row_factory = dict_factory
		return connection

	def ExecuteCommand(self, command):
		print "Executing Command: " + command
		c = None
		connection = None
		try:
			connection = self._GetConnection()
			c = connection.cursor()
			c.execute(command)
			connection.commit()
		except OperationalError, msg:
			print "ExecuteCommand failed: ", msg
		finally:
			if c != None: c.close()
			if connection != None: connection.close()

	def GetQueryResults(self, query):
		c = None
		connection = None
		results = None
		try:
			connection = self._GetConnection()
			c = connection.cursor()
			c.execute(query)
			results = c.fetchall()
		except OperationalError, msg:
			print "ExecuteQuery Failed: ", msg
		finally:
			if c != None: c.close()
			if connection != None: connection.close()
		return results

	def ExecuteFile(self, file_path):
		commands = []
		try:
			f = open(file_path, 'r')
			commands = f.read().split(';')
			f.close()
		except Exception, ex:
			print ex
			raise ex

		for command in commands:
			self.ExecuteCommand(self, command)



