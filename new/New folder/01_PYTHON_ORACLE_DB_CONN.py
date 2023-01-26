import os
#os.chdir("C:\Oracle\instantclient_19_5")
import cx_Oracle


ORACLE_CONNECT = "CG_CU/CGCU@(DESCRIPTION=(SOURCE_ROUTE=OFF)(ADDRESS_LIST=(ADDRESS=(PROTOCOL=TCP)(HOST=localhost)(PORT=1521)))(CONNECT_DATA=(SID=orcl)(SRVR=DEDICATED)))"

orcl = cx_Oracle.connect(ORACLE_CONNECT)
print("Connected to Oracle: " + orcl.version)

sql = "select * from TAB"
curs = orcl.cursor()
curs.execute(sql)

for row in curs:
    print(row)
