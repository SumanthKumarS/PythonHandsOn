import cx_Oracle

con = cx_Oracle.connect('CG_CU/CGCU@127.0.0.1/orcl')

cur = con.cursor()
cur.execute('select * from DEPT order by DEPTNO')
for result in cur:
    print (result)

cur.close()
con.close()
