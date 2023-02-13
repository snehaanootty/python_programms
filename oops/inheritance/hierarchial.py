"""HIERARCHICAL INHERITANCE"""
class A:
    def read(self):
        self.a=int(input("enter the frst num:"))
        self.b=int(input("enter the second num:"))

class B(A):
    def sum(self):
        print("sum is :",self.a+self.b)

class C(A):
    def avg(self):
        print("average is:",(self.a+self.b)/2)
class D(A):
    def product(self):
        print("product is:",self.a*self.b)
ob1=B()
ob1.read()
ob1.sum()
ob2=C()
ob2.read()
ob2.avg()
ob3=D()
ob3.read()
ob3.product()