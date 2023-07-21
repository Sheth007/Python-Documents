import mysql.connector as m

con=m.connect(host="localhost",user="root",database="MYDB",password="")
print(con)
c1=con.cursor()
ID=int(input("Enter id :"))
Name=input("Enter Name :")
Salary=int(input("Enter Salary :"))
Department=input("Enter Department :")
Designation=input("Enter Designation :")
c1.execute ("insert into Employe values ({},'{}',{},'{}','{}');".format(ID,Name,Salary,Department,Designation))
print(c1.rowcount,"rows effected")
con.commit()
con.close()
