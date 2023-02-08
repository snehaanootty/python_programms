dic={"name":"amaya","age":20,"place":"vadakara"}
print(dic)
#
#
"""adding elements in dictionary"""
# dc={}
num=int(input("enter the number:"))
for i in range(num):
    keyy=int(input("enter the key:"))
    valuee=input("enter the value:")
    dc.update({keyy:valuee})
print(dc)
#
dic={"name":"amaya","age":20,"place":"vadakara"}
for i in dic.keys():
    print(i)
print()
for i in dic.values():
    print(i)
print()
for i in dic.items():
    print(i)
print()
for i,j in dic.items():
    print(i,j)
#
x=dic.get("name")
print(x)


dic1={"name":"amaya","age":20,"place":"vadakara"}
print(dic1["name"])
x=dic1.get("name")
print(x)
print(dic1.keys())
print(dic1.values())
print(dic1.items())

dic1["name"]="vishnu"
print(dic1)

dic1.update({"name":"anu"})
print(dic1)

dic1.update({"color":"red"})
print(dic1)

dic1.pop("age")
print(dic1)
dic1.popitem()
print(dic1)

"""NESTED DICTIONARY"""
op={"student1":{"name":"anu","age":19},"student2":{"name":"manj","age":20}}
print(op)
print(op["student1"]["age"])
op["student2"]["name"]="amal"
print(op)
op.update({"student1":{"name":"liya"}})
print(op)