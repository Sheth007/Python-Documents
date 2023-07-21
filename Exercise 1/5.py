class Human:
    def input_human(self):
        self.first_name=input("Enter first name :")
        self.last_name=input("Enter last name :")
    def display_human(self):
        print("First name is :",self.first_name)
        print("ALst name is : ",self.last_name)

class Employee(Human):
    def input_emp(self):
        self.company=input("Enter company name :")
        self.level=input("Enter company level :")
    def display_emp(self):
        print("Company name is : ",self.company)
        print("Comopany level is :",self.level)

eh=Employee()
eh.input_human()
eh.display_human()
eh.input_emp()
eh.display_emp()