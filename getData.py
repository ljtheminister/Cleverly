'''
class pullDatabase:
    def __init__(self, db, dsn_name, table_name, query):
	self.db = db
	self.dsn_name = dsn_name
	self.table = table_name
	self.query = query



    def connect(cnxn_str):
	cnxn = pyodbc.connect(conn_str)
	return cnxn

import re

steam = re.compile('STE', re.IGNORECASE)
result = [x for x in names if steam.search(x)]
'''
import csv
import pyodbc

cnxn = pyodbc.connect("DSN=Anderson;UID=jcm2199;PWD=vanamali")
cursor = cnxn.cursor()

#get database names
q = 'SELECT NAME FROM SYS.DATABASES'
cursor.execute(q)
databases = cursor.fetchall()
databases = ['345', '560']

#get table names
q = 'Use [%s]'%('Weather')
cursor.execute(q)
q = "SELECT * FROM INFORMATION_SCHEMA.TABLES WHERE TABLE_TYPE='BASE TABLE'"
cursor.execute(q)
tables = cursor.fetchall()
table_names = ["[%s].%s.[%s]"%(x[0],x[1],x[2]) for x in tables]
'''
q = "SELECT * FROM INFORMATION_SCHEMA.TABLES"
cursor.execute(q)
all_tables = cursor.fetchall()
'''

file_dir = './data/'+'Weather/'

for table in table_names:
    try:
	q = "SELECT * FROM %s"%(table)
	cursor.execute(q)
	results = cursor.fetchall()
	
	with open(file_dir + table+'.csv', 'w') as f:
	    writer = csv.writer(f)	
	    for row in results:
		writer.writerow(row)
    except:
	print table	
