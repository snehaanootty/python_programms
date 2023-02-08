# #LOCAL SCOPE
# def myfunc():
#     x=300
#     print(x)
# myfunc()
#
# #GLOBAL SCOPE
# x=400
# def myfunct():
#     print(x)
# myfunct()
# print(x)

#NONLOCAL

def programming():
    def python():
        nonlocal name
        name="anu"

    def meanstack():
        name="aju"

    def flutter():
        name="manu"

    name="sanjay"
    python()
    print("the coder is " + name)


programming()