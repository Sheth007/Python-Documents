class drawing:
    def getdata(self):
        self.width=int(input("Enter the width"))
        self.length=int(input("Enter the length"))
    def showdata(self):
        print("width",self.width)
        print("length",self.length)
class rect(drawing):
    pass
re=rect()
re.getdata()
re.showdata()
