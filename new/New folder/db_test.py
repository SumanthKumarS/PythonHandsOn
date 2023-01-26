import cx_Oracle
import os
import sys

print(sys.version)
#print(os.environ['ORACLE_HOME'])
print(os.environ['path'])

con = cx_Oracle.connect('CG_CU/CGCU@localhost/orcl')
print (con.version)

con.close()
