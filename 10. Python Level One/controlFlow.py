if 1 > 2: 
    print('yes')
elif 3 == 3:
    print('elif ran')
else:
    print('last')


seq = [1, 2, 3, 4, 5, 6]

for item in seq:
    print(item)


d = {"sam": 1, "frank":2, "dan": 3}

for key in d:
    print("{} : {}".format(key, d[key]))


mypairs = [(1,2), (3,4), (5,6)]

for tup1, tup2 in mypairs:
    print(tup1)
    print(tup2)
    print('---')

i = 1
while i < 5:
    print("i is: {}".format(i))
    i = i+1
    

# range()
mylist = list(range(0, 5))
print(mylist)

mylist = list(range(0, 21, 2))
print(mylist)


for item in range(10):
    print(item)


# List Comprehension
x = [1, 2, 3, 4]
out = []
for num in x:
    out.append(num**2)

print(out)



out2 = [num**2 for num in x]
print(out2)