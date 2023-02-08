f=open("test","r")
print(f.read())
print(f.read(8))
#
print(f.readline())
#
"""USING FOR LOOP"""
for i in f:
    print(i)
f.close()

"""APPEND"""
f=open("test","a")
f.write("python is a oop")
f=open("test","r")
print(f.read())
f.close()

"""WRITE"""
f=open("test","w")
f.write("python is a oops")
f=open("test","r")
print(f.read())


"""SEEK()"""
f=open("test","r")
f.seek(9)
print(f.readline())
f.close()


# """tell()"""
# f=open("test","r")
# f.readline()
# pos=f.tell()
# f.close()
# print("position is:",pos)

# """WAP to read a file line by line and store it in  to a list"""
# def file_read(fna):
#     with open(fna) as f:
#         result=f.readlines()
#     print(result)
# file_read("test")
#

# from shutil import copyfile
# copyfile("test","test1")

"""WAP to """
# dic={ }
# str1="cat rat mat pat rat cat sat cat sat"
# words=str1.split(" ")
# print(words)
# for i in words:
#     if i in dic:
#         dic[i]=dic[i]+1
#     else:
#         dic[i]=1
# print(dic)

# f=open("test","r")
# dic={ }
# for i in f:
#     var=i.split(" ")
#     for j in var:
#         if j not in dic:
#             dic[j]=1
#         else:
#             dic[j]+=1
# print(dic)