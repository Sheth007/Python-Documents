import mysql.connector as m

con=m.connect(host="localhost",user="root",database="MYDB",password="")
print(con)
c1=con.cursor()
c1.execute("create table Employe(ID int(10),Name varchar(20),Salary int(10),Department varchar(20),Designamtion varchar(20));")
print("Table created succesfully")
con.close()