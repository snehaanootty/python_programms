""" LIST ASSSIGNMENT""""   "
#1 sum of all the items in a list
#
list1=[4,9,6,13]
print(list1[0]+list1[1]+list1[2]+list1[3])
#
#2 write a python program to get the largest number from a list
#
list1=[6,2,9,4,7,3]
list1.sort()
print(list1)
#
list2=[7,9,5,23,13]
list2.sort(reverse=True)
print(list2)
#
#3 write a python program to convert a list of chacares into a string
#
s=['p','y','t','h','o','n']
b=''.join(s)
print(b)
#
#4 write a program to multiply all the items in a list
#
my_list=[3,7,4,8]
m=1
for i in my_list:
    m=m*i
print(m)

my_list=[3,7,4,8]
del my_list[1]
print(my_list)

"""Append items in a list"""
ls=[]
n=int(input("enter the numbers limit :"))
for i in range(n):
    num = int(input("enter the numbers:"))
    ls.append(num)
print(ls)