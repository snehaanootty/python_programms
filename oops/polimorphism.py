class Emp:
    def display(self):
        print("hello")
obj=Emp()
obj.display()


class Emp:
    x=100
    def display(self):
        print("hello")
    def sum(self):
        print("sum is",30+20)
    # def dis():
    #     print("without self parameter")
obj=Emp()
obj.display()
obj.sum()
print("value of x is",obj.x)
# ob=Emp
# ob.dis()

#PASSING ARGUMENTS
class Emp:
    def product(self,a,b):
        print("product is is",a*b)
obj=Emp()
obj.product(20,30)
print()#


class Emp:
    def display(self,a,b):
        self.x=a
        self.y=b
    def sum(self):
        print("sum is",self.x+self.y)
    def product(c):
        print("product is",c.x*c.y)
obj=Emp()
obj.display(10,20)
obj.sum()
obj.product()

class Emp:
    def display(self,a,b):
        self.a=a
        self.b=b
    def sum(self):
        print("sum is",self.a+self.b)
    def product(c):
        print("product is",c.a*c.b)
obj=Emp()
obj.display(10,20)
obj.sum()
obj.product()
print()


"""To find factorial of a number with function using arguments and return value"""
class math:
    def fact(self,n):
        fac=1
        for i in range(1,n+1):
            fac=fac*i
        return fac
obj=math()
n=int(input("enter the num:"))
f=obj.fact
print("factorial is:",f)

#RECURSION FACT

class Emp:


    def fact(sl,x):
        if x==1:
            return 1
        else:
            return x*sl.fact(x-1)
            #return x* Emp.fact(sl,x-1)
obj=Emp()
n=int(input("ente"
            "r the num:"))
f=obj.fact(n)
print("factorial is:",f)
