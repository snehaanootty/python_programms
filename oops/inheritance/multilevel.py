"""MULTILEVEL INHERITANCE"""
class A:
    def read(self):
        self.a = int(input("enter the num:"))
        self.b = int(input("enter the num:"))

class B(A):
    def sum(se):
        se.s=se.a+se.b
        print("sum is :", se.s)
class C(B):
    def avg(self):
        print("average is:",self.s/2)
obj=C()
obj.read()
obj.sum()
obj.avg()