"""findall()"""

import re
str1="hello world hai world"
s=re.findall("world",str1)
print(s)

s=re.findall("worlds",str1)
print(s)                    #no matching


d="cat mat rat sat"
sa=re.findall("[crs]",d)
print(sa)

sa=re.findall("[crs]a",d)
print(sa)

d="cat mat rat sat"
ab=re.findall("[^scr]",d)
print(ab)

d="cat mat rat sat 99923 8977 9999"
a=re.findall("\d{3}",d)
print(a)