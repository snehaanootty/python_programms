a,b=int(input("enter the num:")),int(input("enter the num:"))
a,b=b,a
print('a =',a)
print('b=',b)
#
#type casting method-----covert(str(),int()


"""to check whether the given number is postive or negative or 0"""
n=int(input("enter the num:"))
if n>0:
    print("num is postive")
elif n<0:
    print("num is negative")
else:
    print("num is zero")

"""largest of 3 numbers using nested if"""
#
a=int(input("enter the 1 st num:"))
b=int(input("enter the 2 nd num:"))
c=int(input("enter the 3 rd num:"))
if a>b:
    if a>c:
        print(a,"is largest")
    else:
        print(c,"is largest")
elif b>c:
    print(b,"is greater")
else:
    print(c)

"""Reverse of a number using while"""
n=int(input("enter the num:"))
rev=0
# p=1
# s=0
while n>0:
    r=n%10
    rev=rev*10+r

    n=n//10
print("reverse is",rev)
# print("product is",p)
# print("sum is",s)

"""To check num is armstrong num or not"""

n=int(input("enter the num:"))
order=len(str(n))
sum=0
temp=n
while temp>0:
    r=temp%10
    sum=sum+r**order
    temp=temp//10
if (n==sum):
    print("armstrong num")
else:
    print("not armstrong")


"""To check palindrome or not"""
n=int(input("enter the num:"))
rev=0
temp=n
while temp>0:
    r=temp%10
    rev=rev*10+r
    temp=temp//10
if (n==rev):
    print("palindrome")
else:
    print("not palindrome")