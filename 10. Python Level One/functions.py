def my_func(param1='default'):
    """
    THIS IS THE DOCSTRING
    `x=1` 
    """
    print("my first python function {}".format(param1))

my_func()




def hello():
    return 'hello'


res = hello()
print(res)





def addNum(num1, num2):
    if(type(num1) == type(num2) == type(10)):
        return num1+num2
    else:
        return "sorry ,I need integers!"


res = addNum(2, 3)
print(res)


res = addNum("2", "3")
print(res)




# filter
mylist = [1, 2, 3, 4, 5, 6, 7, 8]

def even_bool(num):
    return num%2 == 0

evens = filter(even_bool, mylist)
print(evens)



# Lambda Expression 
evens2 = filter(lambda num: num%2 == 0, mylist)
print(evens2)



# string methods
tweet = "Go Sports! #Sports"
result = tweet.split('#')[1]
print(result)

print('x' in [1, 2, 3])
print('x' in [1, 2, 3, 'x'])