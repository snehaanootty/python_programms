import re
str1="rose and jasmines are flowers"
g=re.sub(" ","*",str1)
print(g)

s=re.sub(" ","*",str1,3)
print(s)