import mysql.connector as m

con=m.connect(host="localhost",user="root",password="")
print(con)
c1=con.cursor()
c1.execute("create database MYDB;")
print("Database created succesfully")
con.close()