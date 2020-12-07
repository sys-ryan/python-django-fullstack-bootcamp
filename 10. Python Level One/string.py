# STRINGS

mystring = 'abcdefg'
print(mystring)
print(mystring[0])

# Slicing
print(mystring[:3])

print(mystring[2:5])

print(mystring[:])
print(mystring[::2])

# upper
print(mystring.upper())

# capitalize
print(mystring.capitalize())

# split
mystring = 'Hello World'
x = mystring.split()
print(x)
mystring = 'Hello/World'
x = mystring.split('/')
print(x)


# Print Formatting
x = "Insert another string here: {}".format("<INSERTED STRING>")
print(x)

x = "Item one : {} \nItem Two : {}".format("dog", "cat")
print(x)

x = "Item one : {y} \nItem Two : {x}".format(x = "dog", y = "cat")
print(x)
