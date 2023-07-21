class parent:
    def show(self):
        print("Parent")
class child(parent):
    def show(self):
        print("Child")
p=parent()
c=child()
p.show()
c.show()