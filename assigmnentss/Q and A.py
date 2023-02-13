str1="amaya"
for i in str1:
    print(i)
    print()
#
#PROGRAM TO PRINT THE TABLE OF THE GIVEN NUMBER
ls=[1,2,3,4,5]
n=2
for i in ls:
    s=n*i
    print(s)
    print()
#
#PROGRAM TO PRINT THE SUM OF GIVEN NUMBERS
ls1=[2,4,5,6,7,1]
s=0
for i in ls1:
    s=s+i
print(s)
#
#SUM OF N NUMBERS
n=int(input("enter the number:"))
s=0
for i in range(1,n):
    s=s+i
print(s)
#
#
#PRINT NUMBERS IN SEQUENCE
for i in range(10):
    print(i,end=" ")
#
#
#PRINT MULTIPLICATION TABLE OF GIVEN NUMBER
n=int(input("enter the number:"))
for i in range(1,11):
    c=n*i
    print(n,"*",i,"=",c)
#
#
#PRINT EVEN NUM USING IN STEPSIZE IN RANGE
n=int(input("enter the num:"))
for i in range(2,n,2):
    print(i)
#
""""##len()-----list##"""
lst=["anu","ammu","anju"]
for i in range(len(lst)):
    print("hello",lst[i])

"""To print fibonacci series using range()"""#0 0  1 2 3 5 8 13
n=int(input("Enter the num:"))
sum=0
a=0
b=1
for i in range(n):
    sum=a+b
    print(a)
    a=b
    b=sum
#/
n=int(input("Enter the num:"))
a,b=0,1
print(a)
print(b)
for i in range(3,n+1):
    sum=a+b
    print(sum)
    a,b=b,sum

"""Prime number"""
n=int(input("enter the num:"))
f=0
#n=5----5%1=0,5%2==1,5%3==2,5%4==1,5%5==0
if n==1:
    print("not defined")
else:
    for i in range(1,n+1):#1----n
        if n%i==0:
            f=f+1#1,2
    if f==2:
        print("prime")
    else:
        print("not prime")

# ###
#

"""1. To create and print a list where values are square of numbers b/w 1 and 30(both included)"""

def list_creation():
    l=list()
    for i in range(1,31):
        l.append(i**2)
    print(l)
list_creation()



"""3.Assign a different name to  function and call it through the new name"""

def sum(a,b):
    c=a+b
    return c
s=sum
print(s(2,4))


""" 4. Generate a pyton list of all the even numbers b/w 4 to 30"""
def even():
    l=[]
    for i in range(4,31):
        if i%2==0:
            l.append(i)
    print(l)
even()


""" 5.Function returns a tuple"""

def person():
    return "ammu",20,"software"
print(person())



"""6.Define a function which counts vowels and consonent"""

word=input("enter the word")
def count(val):
    vowels=0
    consonent=0
    v=["a","i","e","o","u"]
    for i in word:
        if i in v:
            vowels=vowels+1
        else:
            consonent=consonent+1
    print("the count of vowels is:",vowels)
    print("the count of consonent is:", consonent)
count(word)

"""7.present or absent"""

def stdnts(n):
    l=[1,2,3,4,5,6]
    if n in l:
        print("present")
    else:
        print("absent")
stdnts(4)



"""8.Return the maximum od 3 numbers"""

def max(a,b,c):
    if a>b and a>c:
        print("a is max")
    elif b>c and b>a:
        print("b is max")
    elif c>a and c>b:
        print("c is max")
max(3,6,1)

"""" 2 numbers of arguments and return the sum"""
def add(a,b):
    print("the sum is",a+b)
add(2,3)

"""function that accepts different values as parameters and returns a list"""
def myfunc(*n):
    l=[]
    for i in n:
        l.append(i)
    print(l)
myfunc("anu","aju","ammu")

""" function that accepts 2 values and return its sum ,subtraction,multiplication"""
def operations(a,b):
    print("the sum is",a+b)
    print("the subtraction is ",a-b)
    print("the multiply is ",a*b)
operations(4,5)

"""access inner function in a function"""
def test(a):
    def add(b):
        nonlocal a
        a+=1
        return a+b
    return add(8)
func=test(4)
print(func)

#program to print 1 to 10
i=1
while i<=10:
    print(i)
    i=i+1


#print table of given number
i=1
num=int(input("enter the number:"))
while i<=10:
    print("%d x %d=%d\n"%(num,i,num*i))
    i=i+1

#Sum of even numbers
n=int(input("enter the number"))
i=1
s=0
while i<=n:
    if(i%2==0):
        s=s+i
    i=i+1
print(s)

#AVG OG 5 NUMBERS
i=1
s=0
while i<=5:
    n=int(input("enter the %d:"%(i)))
    s=s+n
    i=i+1
avg=s/5
print(avg)


#ADDING ELEMENT TO A LIST USING WHILE LOOP
n=int(input("enter the number:"))
a=[]
i=0
while i<=n:
    a.append(i)
    i=i+1
print(a)




#PRINT SQUARE OF NUMBERS
n=int(input("enter the number:"))
s=0
i=1
while i<=n:
    s=i*i
    i=i+1
print(s)

#REVERSE A NUMBER
num=int(input("enter the number:"))
rev=0
while num!=0:
    digit=num%10
    rev=rev*10+digit
    num=num//10
print(rev)

""" another method """
num=int(input("enter num:"))
i=0
str1=str(num)
while i<len(str1):
    i=i+1
print(str1[::-1])



#PRINT EVEN &ODD B/W 1 TO 100
n=int(input("enter the number:"))
i=1
while i<=n:
    print(i,end=" ")
    if i%2==0:
        print("even")
    else:
        print("odd")
    i=i+1
# str1="amaya"
# for i in str1:
#     print(i)
#     print()
#
# #PROGRAM TO PRINT THE TABLE OF THE GIVEN NUMBER
# ls=[1,2,3,4,5]
# n=2
# for i in ls:
#     s=n*i
#     print(s)
#     print()
#
# #PROGRAM TO PRINT THE SUM OF GIVEN NUMBERS
# ls1=[2,4,5,6,7,1]
# s=0
# for i in ls1:
#     s=s+i
# print(s)
#
# #SUM OF N NUMBERS
# n=int(input("enter the number:"))
# s=0
# for i in range(1,n):
#     s=s+i
# print(s)
#
#
# #PRINT NUMBERS IN SEQUENCE
# for i in range(10):
#     print(i,end=" ")
#
#
# #PRINT MULTIPLICATION TABLE OF GIVEN NUMBER
# n=int(input("enter the number:"))
# for i in range(1,11):
#     c=n*i
#     print(n,"*",i,"=",c)
#
#
# #PRINT EVEN NUM USING IN STEPSIZE IN RANGE
# n=int(input("enter the num:"))
# for i in range(2,n,2):
#     print(i)
#
# """"##len()-----list##"""
# lst=["anu","ammu","anju"]
# for i in range(len(lst)):
#     print("hello",lst[i])

"""To print fibonacci series using range()"""#0 0  1 2 3 5 8 13
# n=int(input("Enter the num:"))
# sum=0
# a=0
# b=1
# for i in range(n):
#     sum=a+b
#     print(a)
#     a=b
#     b=sum
# #/
n=int(input("Enter the num:"))
a,b=0,1
print(a)
print(b)
for i in range(3,n+1):
    sum=a+b
    print(sum)
    a,b=b,sum

"""Prime number"""
n=int(input("enter the num:"))
f=0
#n=5----5%1=0,5%2==1,5%3==2,5%4==1,5%5==0
if n==1:
    print("not defined")
else:
    for i in range(1,n+1):#1----n
        if n%i==0:
            f=f+1#1,2
    if f==2:
        print("prime")
    else:
        print("not prime")

###
#
#for else
for i in "amaya":
    print(i)
else:
    print("completed")

"""BREAK"""
l=[10,20,30,40,50,100,200,250]
for i in l:
    print(i)
    if (i==100):
        break
print()
#
"""CONTINUE"""
l=[10,20,30,40,50,100,200,250]
for i in l:
    if i==100:
        continue
      print(i)
