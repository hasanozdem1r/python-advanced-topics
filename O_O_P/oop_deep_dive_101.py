"""
An object has two characteristics ; attributes, behaviour
"""
# When class is defined, only the description for the object is defined. Therefore, no memory or storage is allocated.

# Methods are functions defined inside the body of a class. They are used to define the behaviors of an object.


class Parrot:
    # class attribute
    species: str = "bird"

    # instance attribute
    def __init__(self, name, age):
        self.name = name
        self.age = age

    # instance method
    def sing(self, song):
        return "{} sings {}".format(self.name, song)

    def dance(self):
        return "{} is now dancing".format(self.name)


# instantiate the Parrot class
blu = Parrot("Blu", 10)
woo = Parrot("Woo", 15)

# access the class attributes
print("Blu is a {}".format(blu.__class__.species))
print("Woo is also a {}".format(woo.__class__.species))

# access the instance attributes
print("{} is {} years old".format(blu.name, blu.age))
print("{} is {} years old".format(woo.name, woo.age))

# call our instance methods
print(blu.sing("'Happy'"))
print(blu.dance())
