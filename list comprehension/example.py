"""LIST COMPREHENSION"""
l=[x+3 for x in [1,2,3,4]]
print(l)


l=[x for x in range(25) if x%2==0]
print(l)

"""vowels"""
str1=input("enter the string")
v=[x for x in str1 if x in ["a","e","i","o","u"]]
print(v)

"""split"""

str1="hello world"
words=str1.split( )
print(words)
letters=[i[0]  for i in words]
print(letters)

"""print e character "e" in this colors"""
colors=['red','white','green','pink']
l=[i for i in colors if "e" in i]
print(l)

colors=['red','white','green','pink']
ls=[i for i in colors if i!="green"]
print(ls)

# """builtin methods"""
# colors=['red','white','green','pink']
# ls=[i.upper() for i in colors]
# print(ls)
#
# colors=['red','white','green','pink']
# ls=["hello" for i in colors]
# print(ls)
#
# colors=['red','white','green','pink']
# ls=[i if i!="pink"
#     else "blue"for i in colors]
# print(ls)
# def sum():
#     a,b=
# s=sum()
# print("sum is",s)