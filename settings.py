from database import Database
import pyodbc

Anderson = Database('{SQL Server}', 'anderson.ldeo.columbia.edu', '345', 'jcm2199', 'vanamali')

#cnxn_str = 'DRIVER=%s;SERVER=%s;DATABASE=%s;UID=%s;PWD=%s'%(Anderson.driver, Anderson.server, Anderson.database, Anderson.uid, Anderson.pwd)

#cnxn = pyodbc.connect(cnxn_str)


#cnxn = pyodbc.connect('DSN=Anderson;UID=jcm2199;PWD=vanamali')
#cnxn = pyodbc.connect('DSN=Anderson;UID=Hooshmand;PWD=Breakit68')
