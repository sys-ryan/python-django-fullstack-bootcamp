s = "GLOBAL VARIABLE!"

def func():
    print s

func()
print(s)


def func():
    global s
    s = 50
    print s

func()
print(s)


def func():
    mylocal = 10
    print(locals())
    print(globals())

func()


def hello(name='ryan'):
    print("THE HELLO() FUNCTION HAS BEEN RUN")

    def greet():
        return "THIS STRING IS INSIDE GREET()"

    def welcome():
        return "THIS STRING IS INSIDE WELCOME()"

    if name == 'ryan':
        return greet
    else:
        return welcome


    # print(greet())
    # print(welcome())
    # print("End of Hello()")

hello()

x = hello()
print(x())






def hello():
    return "Hi Ryan"

def other(func):
    print("HELLO")
    print(func())

other(hello)




def new_decorator(func):
    
    def wrap_func():
        print("CODE HERER BEFORE EXECUTING FUNC")
        func()
        print("FUNC() HAS BEEN CALLED")

    return wrap_func

@new_decorator
def func_needs_decorator():
    print("THIS FUNCTION IS IN NEED OF A DECORATOR")

# func_needs_decorator = new_decorator(func_needs_decorator)
func_needs_decorator()


