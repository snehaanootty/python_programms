# x= lambda a : a + 10
# print(x(5))
#
# y= lambda a,b: a+b
# print(y(6,12))
#
# def myfun(n):
#     return lambda a: a * n
# mydouble=myfun(2)
# print(mydouble(11))
#
# """ WAP TO CREATE A FUNCTION THAT TAKES ONE ARGUMENT AND THAT ARGUMENT WILL BE MULTIPLIED WITH A  UNKNOWN
#     GIVEN NUMBER"""
#
# def myfun(n):
#     return lambda a: a * n
# mydouble=myfun(2)
# print(mydouble(11))
#
# """ wap to prgrm to filter  list of integers in a list"""
# #####FILTER()#####
# num=[1,2,3,4,5]
# even_nums=list(filter(lambda a: a%2==0,num))
# print(even_nums)
# odd_nums=list(filter(lambda a:a%2==1,num))
# print(odd_nums)
#
# #lambda with if else
# max=lambda a,b: a if (a>b) else b
# print((max(5,8)))
# max1=lambda a,b,c: a if (a>b and a>c) else b if (b>a and b>c) else c
# print(max1(5,8,10))
# print()
#
# """####MAP()####"""
# def myfun(a,b):
#     return a+b
# x=map(myfun,('apple','orange'),('mango','strawberry'))
# print(list(x))
# print()
#
# li=[4,7,9,5,6,8]
# final_list=list(map(lambda a:a*2,li))
# print(final_list)
#
# animal=['dog','cat','parrot']
# new=list(map(lambda a:a.upper(),animal))
# print(new)
# print()
#
# """###FILTER###"""
# ages = [5, 12, 17, 18, 24, 32]
#
# def myFunc(x):
#   if x < 18:
#     return False
#   else:
#     return True
#
# adults = filter(myFunc, ages)
#
# for x in adults:
#   print(x)
#
#
# """###REDUCE()###"""
# from functools import reduce
# product=reduce(lambda x,y:x*y (1,2,3,4,5))
# print(product)

# """13-1-23 LAMBDA FUNCTION"""#SIMPLE PROGRAM
#
# add=lambda a,b:a+b
# print(add(10,20))
#
# largest=lambda a,b:a if(a>b) else b
# print(largest(100,300))
#
# """FILTER MAP REDUCE"""
# #FILTER
# l=[20,3,4,5,11,90]
# lst=list(filter(lambda x:x%2==0,l))
# print(lst)
#
# #map
# l=[20,3,4,5,11,90]
# lst1=list(map(lambda x:x>10,l))
# print(lst1)
#
# #reduce
# from functools import reduce
# ls=[2,3,4,5]
# product=reduce(lambda x,y:x*y,ls)
# print(product)