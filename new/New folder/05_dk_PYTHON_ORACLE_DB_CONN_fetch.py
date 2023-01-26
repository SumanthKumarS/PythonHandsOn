import os
import cx_Oracle

con = cx_Oracle.connect('CG_CU/CGCU@127.0.0.1/orcl')

cur = con.cursor()
cur.execute('select * from EMP order by DEPTNO')

#for loop to access entire records in a table
'''for result in cur:
    print (result)'''

#using FETCH() options
'''row = cur.fetchone()
print (row)'''

'''row = cur.fetchone()
print (row)'''

#The fetchmany() method returns a list of tuples.
#Here the numRows parameter specifices that three rows should be returned.
'''res = cur.fetchmany(numRows=3)
print (res)'''

#fetchall() method to return all rows. The output is a list (Python's name for an array) of tuples.
#Each tuple contains the data for one row.
res = cur.fetchall()
print (res)

cur.close()
con.close()
