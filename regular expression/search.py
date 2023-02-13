"""search()"""

import re
str1="classes will start at 10 am"
s=re.search("\s",str1)
print(s)
print(s.start())

s2=re.search("py",str1)
print(s2)

str1="class will start at 10am"
s=re.search("^class.*10am$",str1)
if s:
    print("find")
else:
    print("not find")