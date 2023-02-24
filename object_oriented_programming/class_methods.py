"""
A class is a code template for creating objects
An object is created using the constructor of the class. This object will then be called the instance of the class.
Python has three different method types. static, class and instance method
"""

# living creature
class Organism:

    @staticmethod
    def who_am_i():
        return "I am an organism"
    
    @classmethod
    def who_you_are(cls,name:str):
        return f"I am {name}"
    
    def who_they_are(self):
        return "They are instance class and they can access all class methods"

class Human:
    pass

if __name__=="__main__":
    # call static method
    print(Organism.who_am_i())
    # call class method (1)
    print(Organism.who_you_are(name="Hasan"))
    # call class method (2)
    obj=Organism()
    print(obj.who_you_are(name="Hasan"))
    # call instance method
    obj2=Organism
    print(obj.who_they_are())