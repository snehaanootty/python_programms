"""PHONE NO VALIDATION"""
import re
def isValid(s):
    Pattern = re.compile("(0|91)?[6-9][0-9]{9}")
    return Pattern.fullmatch(s)
s=input("num:")
if (isValid(s)):
    print("Valid Number")
else:
    print("Invalid Number")


import re                         # Importing re module
n=input('Enter Mobile number :')  # Reading input from the user
r=re.fullmatch('[6-9][0-9]{9}',n) # calling fullmatch function by passing pattern and n
if r!=None:                       # checking whether it is none or not
     print('Valid Number')
else:
     print('Not a valid number')