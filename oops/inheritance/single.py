"""SINGLE INHERITANCE"""
class A:
    def displayA(self):
        print("base method")
class B(A):
    def displayB(self):
        print("derived method")
ob=B()
ob.displayA()
ob.displayB()

"""WAP TO FIND SUM OF 2 NUMBERS"""
class A:
    def read(self,a,b):
        self.x=a
        self.y=b

class B(A):
    def sum(se):
        print("sum is :",se.x+se.y)
obj=B()
obj.read(10,40)
obj.sum()