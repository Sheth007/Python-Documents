class GrandM:
    def action(self):
        self.height=int(input("Enter height :"))
        self.color=input("Enter color :")
    def get(self):
        print("Height is :",self.height)
        print("Color is : ",self.color)
        
class Mother(GrandM):
    def action1(self):
        self.eyecolor=input("Enter eye color :")
    def get1(self):
        print("Eye colort is ",self.eyecolor)
        
class daughter(Mother):
    pass

dm=daughter()
dm.action()
dm.action1()
dm.get()
dm.get1()
