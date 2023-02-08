#for else
for i in "amaya":
    print(i)
else:
    print("completed")

"""BREAK"""
l=[10,20,30,40,50,100,200,250]
for i in l:
    print(i)
    if (i==100):
        break
print()
#
"""CONTINUE"""
l=[10,20,30,40,50,100,200,250]
for i in l:
    if i==100:
        continue
    print(i)