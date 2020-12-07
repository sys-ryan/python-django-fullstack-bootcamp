# Lists
mylist = [1, 2, 3, 4]

listone = ["y", 'y', 'z']

#append()
mylist.append(listone)
print(mylist)


#extend()
mylist = [1, 2, 3, 4]
listone = ["y", 'y', 'z']
mylist.extend(listone)
print(mylist)


# pop
item = mylist.pop()
print(mylist)
print(item)

item = mylist.pop(0)
print(item)

#reverse()
print(mylist)
mylist.reverse()
print(mylist)


#sort()
mylist = [4, 6, 1, 7 ,45]
mylist.sort()
print(mylist)


# method list
mylist = [1, 2, ['x', 'y', 'z']]
print(mylist[2][1])


#matrix
matrix = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]

#LIST COMPREHENSION
first_col = [row[0] for row in matrix]
print(first_col)