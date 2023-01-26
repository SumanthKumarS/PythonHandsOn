import cx_Oracle   
con=cx_Oracle.connect('CG_CU/CGCU@localhost/orcl')   
print(con.version)   
con.close()
