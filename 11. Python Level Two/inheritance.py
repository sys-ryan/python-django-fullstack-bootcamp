# INHERITANCE
class Animal():

    def __init__(self):
        print("ANIMAL CREATED")

    def whoAmI(self):
        print("ANIMAL")

    def eat(self):
        print("EATING")


mya = Animal()
mya.whoAmI()
mya.eat()


class Dog(Animal):

    def __init__(self):
        Animal.__init__(self)
        print("DOG CREATED")

    def bark(self):
        print("WOOF")

    def eat(self):
        print("DOG EATING")

myd = Dog()
myd.whoAmI()
myd.eat()
myd.bark()



# SPECIAL METHODS

class Book():
    def __init__(self, title, author, pages):
        self.title = title
        self.author = author
        self.pages = pages


    #string reperesentation of the object
    def __str__(self):
        return "Title: {}, Author: {}, Pages: {}".format(self.title, self.author, self.pages)

    
    def __len__(self):
        return self.pages

    def __del__(self):
        print("a book is destroyed")
        



b = Book("Python", "jose", 200)
print(b)
print(len(b))

del b
