my_list=[6,9,7,3,6,[4,7,4,9],8]
print(my_list[5][2])

"""CHANGE"""
my_list[1]=10
print(my_list)
#
"""LIST METHODS"""
"""append"""
lst=[4,7,8,9,"hello",[6,9,8]]
lst.append("anu")
print(lst)
lst.append([1,2,3,4])
print(lst)

"""extend"""
lst=[4,7,8,9,"hello",[6,9,8]]
lst.extend([1,2,3,4])
print(lst)

"""insert"""
lst=[4,7,8,9,"hello",[6,9,8]]
lst.insert(4,"python")
print(lst)
#
list1=['love',6544,'hello']
#
print(lst[-2])
print(lst[2])
print(type(list1))
#
"""Access item from a list"""
lst=[1,2,3,4,5]
lst2=["aa",["ss","dd","ee"],"hh"]
lst2[1].insert(1,"mm")
print(lst2)
#
"""COUNT"""
lst1=[1,2,3,4,5,2,3,1,4,6,4]
x=lst1.count(4)
print(x)
#
"""INDEX"""
ls=["apple","mango","orange"]
y=ls.index("apple")
print

"""----DELETING ITEMS----"""
"""pop"""
lst3=[4,7,8,9,"hello",[6,9,8]]
lst3.pop()
print(lst3)
lst3.pop(2)
print(lst3)

"""remove"""
lst3.remove("hello")
print(lst3)

"""clear"""
lst3.clear()
print(lst3)

"""reverse"""
lst3=["apple","mango","orange"]
lst3.reverse()
print(lst3)

"""sort"""
ls12=[3,1,4,6,4]
ls12.sort()
print(ls12)

#descending
ls12.sort(reverse=True)
print(ls12)

"""copy"""
my_list=["apple","orange"]
print(my_list)
print(my_list.copy())