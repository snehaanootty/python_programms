class A:
    def __init__(self,name):
        print("parameterized constructor")
        self.na=name
    def display(self):
        print("name is :",self.na)
obj=A("anu")
obj.display()