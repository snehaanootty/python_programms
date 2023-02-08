try:
    a=int(input("enter the num:"))
    b=int(input("enter the num:"))
    c=a/b
    print("result is :",c)
except Exception as ex:
    print(ex)
except ZeroDivisionError  as er:
    print(er)
except ValueError as er:
    print(er)