# def tri(k):
#     if(k>0):
#         result=k+tri(k-1)
#         print(result)
#     else:
#
#         result=0
#     return result
# print("example")
# tri(5)
#
#FACTORIAL
def factorial(no):
    if no==1:
        return 1                              #5*4!----5*24=120
    else:                                     #4*3!----4*6=24
        return no*factorial(no-1)             #3*2!----3*2=6
f=factorial(5)
print("factorial of 5 is",f)


# #SUM OF GIVEN NUMBERS
def num(no):
    if no==1:
        return 1
    else:
        x = no+num(no-1)
        print()
        return x

print(num(5))