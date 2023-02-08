#islower()
a='python'
print(a.islower())

#isupper()
b='luminar'
print(b.isupper())

#isalpha()
c='anu123'
print(c.isalpha())

#isalnum()
d='anumol45'
print(d.isalnum())

#istitle()
e='Eagle eyes'
print(e.istitle())
#capitalize()
a="python Django"
print(a.capitalize())

#lower()
b='python'
print(b.lower())

#upper()
c='Python'
print(c.upper())

#swapcase()
d="luminar"
print(d.swapcase())

#title()
e="welcome to python programming"
print(e.title())

#len()
f='banana'
x=len(f)
print(x)
#find()    return -1 if the value is not find
a='luminar technolab'
print(a.find('l'))
print(a.find('o'))
print(a.find('m',1,6))
print(a.find('l',8,16))
print(a.find('u',4,9))   #returns -1

#index()   return value error if string is not found
b='amala paul'
print(b.index('l'))
print(b.index('m',0,4))
#print(b.index('x'))      #value error

#rfind()
c='this is a good is example'
print(c.rfind('is'))   #last index will be exxecuted

#count()
f="eagle eyes"
print(f.count('e'))
print(f.count('e',0,5))
#string datatype
str1="hello world"
age="12"
print(type(str1))

#string indexxing
str2="hello world"
print(str2[4])
print(str2[5])
print(str2[9])
print(str2[-1])
print(str2[-5])

#string slicing
str3="hello world"
print(str3[0:4])
print(str3[6:9])
print(str3[0:])
print(str3[:6])
print(str3[-3:])
print(str3[:-3])
print(str3[::-1])
print(str3[::-2])