class Sample():
    pass

x = Sample()
print(type(x))


class Dog():

    # CLASS OBJECT ATTRIBUTE
    species = "mammal"

    def __init__(self, breed, name):
        self.breed = breed
        self.name = name

mydog = Dog(breed="Lab", name="Sammy")
print(type(mydog))
print(mydog)
print(mydog.breed)
print(mydog.name)
print(mydog.species)

# otherDog = Dog(breed="Huskie")
# print(otherDog.breed)




class Circle():

    pi = 3.14

    def __init__(self, radius=1):
        self.radius = radius

    def area(self):
        return self.radius * self.radius * Circle.pi

    def set_radius(self, new_r):
        self.radius = new_r


myc = Circle(3)
print(myc.radius)
print(myc.area)
print(myc.area())

myc.radius = 100
print(myc.area())

myc.set_radius(10)
print(myc.area())