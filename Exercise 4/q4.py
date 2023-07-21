import mysql.connector as m

con=m.connect(host="localhost",user="root",database="MYDB",password="")
print(con)
mycursor=con.cursor()
mycursor.execute("select * from Employe;")
records=mycursor.fetchall()
print(records)
con.close()
