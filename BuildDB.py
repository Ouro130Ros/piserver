import sqlite3
from sqlite3 import OperationalError
import os
import glob

def executeCommandsFromFile(file_path, cursor):
	print 'Executing ' + file_path
	f = open(file_path, 'r')
	sqlContents = f.read()
	f.close()

	commands = sqlContents.split(';')
	for command in commands:
		try:
			cursor.execute(command)
		except OperationalError, msg:
			print 'Command Skipped: ', msg

conn = sqlite3.connect('boardgames.db')
c = conn.cursor()

filesToExecute = glob.glob(os.path.join(os.getcwd(), 'DataModel', 'BoardGames', 'DDLS', '*'))
for file in filesToExecute:
	executeCommandsFromFile(file, c)


c.close()
conn.close()