"""
Inheritance is a way of creating a new class for using details of an existing class without modifying it.
The newly formed class is a derived class (or child class). Similarly, the existing class is a base class (or parent class).
"""
# parent class
class Bird:

    def __init__(self):
        print("Bird is ready | BIRD CLASS")

    def whoisThis(self):
        print("Bird")

    def swim(self):
        print("Swim faster")


# child class
class Penguin(Bird):

    def __init__(self):
        # call super() function
        super().__init__()
        print("Penguin is ready | PENGUIN CLASS")

    def whoisThis(self):
        print("Penguin")

    def run(self):
        print("Run faster")


peggy = Penguin()
peggy.whoisThis()
peggy.swim()
peggy.run()