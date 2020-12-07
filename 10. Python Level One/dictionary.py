#Dictionaries 
my_stuff = {"key1" : "value1", "key2" : "value2", "key3":{'123':[1, 2, 'grabMe']}}
print(my_stuff['key1'])

print(my_stuff)

print(my_stuff['key3']['123'][2].upper())



my_stuff = {'lunch':'pizza', 'bfast':'eggs'}
print(my_stuff['lunch'])

my_stuff['lunch'] = 'burger'
print(my_stuff['lunch'])