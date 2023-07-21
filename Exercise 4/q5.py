import mysql.connector as m

con=m.connect(host="localhost",user="root",database="MYDB",password="")
print(con)
c1=con.cursor()
c1.execute("delete from Employe where Department = 'computer';")
print(c1.rowcount,"row effedted")
con.commit()
con.close()
