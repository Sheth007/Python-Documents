class Employee:
    def getEmp(self):
        self.emp_id=int(input("Enter your id"))
        self.name=input("Enter your name")
        self.salary=int(input("Enter your salary"))
        self.date_of_join=input("Enter your dob")
    def showEmp(self):
        print("Id is ",self.emp_id)
        print("Name is ",self.name)
        print("Salary is ",self.salary)
        print("date of birth is ",self.date_of_join)
em=Employee()
em.getEmp()
em.showEmp()
        
