# #largest among three no
n1=int(input("enter the 1st no:"))
n2=int(input("enter the 2nd no:"))
n3=int(input("enter the 3rd no:"))
if (n1>=n2 and n1>=n2):
    print("n1 is greater")
elif(n2>=n1 and n2>=n1):
    print("n2 is greater")
else:
    print("n3 is greater")

#FIND PERCENTAGE AND GRADEi
phy=int(input("enter your marks:"))
math=int(input("enter your marks:"))
ch=int(input("enter your marks:"))
bio=int(input("enter your marks:"))
com=int(input("enter your marks:"))
perc=((phy+math+ch+bio+com)/500*100)
print(perc)
if perc>=90:
    print("grade A")
elif perc>=80 and perc<=89:
    print("grade B")
elif perc>=70 and perc<=79:
    print("grade c")
elif perc>=60 and perc<=69:
    print("grade D")
elif perc>=50 and perc<=59:
    print("grade E")
elif perc<=40:
    print("failed")
else:
    print("invalid")

