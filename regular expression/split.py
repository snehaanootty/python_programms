import re
str2="class will start at 10am "
s=re.split(" ",str2)
print(s)

s1=re.split("a",str2)
print(s1)

s2=re.split(" ",str2,3)
print(s2)