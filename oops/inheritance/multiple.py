"""MULTIPLE INHERITANCE"""
class A:
    def read(self):
        self.a=input("enter the name:")
        self.b=int(input("enter the age:"))
        self.c=input("enter the address:")
        self.d=int(input("enter the phone no:"))
class B:
    def details(self):
        self.f=int(input("enter the salary:"))
class C(A,B):
    def employee(self):
       print("NAME:",self.a)

       print("AGE:", self.b)
       print("ADDRESS:", self.c)
       print("PHONE:", self.d)
       print("SALARY", self.f)
obj=C()
obj.read()
obj.details()
obj.employee()