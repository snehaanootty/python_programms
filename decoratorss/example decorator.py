#DECORATERS
def make_pretty(func):
    def inner():
        print("I got decorated")
        func()
    return inner
@make_pretty
def ordinary():
    print("i am ordinary")
ordinary()

#CALCULATOR
def calculator(func):
    def add(a,b):
        print("addition:",a+b)
        return func(a,b)
    return add
@calculator
def multi(a,b):
    print("multiplication:",a*b)
multi(4,5)
def divide(a,b):
    if a==0 or b==0:
        print("not divide")
    else:
        print("divide:",a/b)
divide(0,0)
def sub(a,b):
    print("subtraction:",a-b)
sub(8,4)

#frstclass function
def upper_decor(fun):
    def wrapper():
        result=fun()
        return result.upper()
    return wrapper()
def hello_name():
    return "hello"
f=upper_decor(hello_name)
print(f)

#decorate
def upper_decor(fun):
    def wrapper(name):
        result=fun(name)
        return result.upper()
    return wrapper
@upper_decor
def hello_name(name):
    return "hello " + name
print(hello_name("arya"))