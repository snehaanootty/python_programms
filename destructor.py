class A:
    def __init__(self,name):
        print("parameterized constructor")
        self.na=name
    def _del_(self):
        print("destructors")
    def display(self):
        print("name is :",self.na)
obj=A("anu")
del obj
obj.display()