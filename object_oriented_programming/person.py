from typing import Any


class Person:

    # init method is used to create an instance of the class.
    def __init__(self, person_id: int, full_name: str, age: int,
                 country_of_residence: str) -> None:
        self.person_id = person_id
        self.full_name = full_name
        self.age = age
        self.country_of_residence = country_of_residence

    # str method is useful when we want to use instances of our class in a print statement
    def __str__(self) -> str:
        return f"Full-name:{self.full_name} - Age:{self.age} - Country of Residence:{self.country_of_residence}"

    def __setitem__(self, key: Any, value: Any):
        if key == 'person_id':
            self.person_id = value
        elif key == 'full_name':
            self.full_name = value
        elif key == 'age':
            self.age = value
        elif key == 'country_of_residence':
            self.country_of_residence = value
        else:
            raise KeyError(
                f"{key} is not a valid attribute of the Person class")

    def __getitem__(self, key):
        if key == 'person_id':
            return self.person_id
        elif key == 'full_name':
            return self.full_name
        elif key == 'age':
            return self.age
        elif key == 'country_of_residence':
            return self.country_of_residence
        else:
            raise KeyError(
                f"{key} is not a valid attribute of the Person class")

    def __delitem__(self, key):
        """
        Delete attribute of a Person class
        :param key: attribute
        :raises KeyError: if given attribute is not existed
        """
        if key == 'person_id':
            del self.person_id
        elif key == 'full_name':
            del self.full_name
        elif key == 'age':
            del self.age
        elif key == 'country_of_residence':
            del self.country_of_residence
        else:
            raise KeyError(
                f"{key} is not a valid attribute of the Person class")

    #  add method is called when using the + operator.
    def __add__(self, second_obj):
        if not isinstance(second_obj, Person):
            raise TypeError(
                f"Cannot concatenate Person with {type(second_obj).__name__}")

        person_id = self.person_id + second_obj.person_id
        full_name = self.full_name + ' ' + second_obj.full_name
        age = self.age + second_obj.age
        country_of_residence = self.country_of_residence + ' & ' + second_obj.country_of_residence
        return Person(person_id, full_name, age, country_of_residence)


if __name__ == "__main__":
    # initialize p1
    p1 = Person(person_id=1,
                full_name="Hasan Ozdemir",
                age=25,
                country_of_residence="Türkiye")
    # call __str__ method
    print(p1)

    # initialize p2 with typo
    p2 = Person(person_id=2,
                full_name="Jon Doe",
                age=215,
                country_of_residence="America")

    # fix type by using __setitem__
    p2["full_name"] = "John Doe"
    p2["age"] = 25
    print(p2)

    # get item using __getitem__
    print(f"Name of p1: {p1['full_name']}")

    # p3 = Person(1, 'John Doe', 30, 'USA')
    # del p3['full_name']
    # print(p3.full_name) # Raises AttributeError: 'Person' object has no attribute 'full_name'

    # add two object with __add__ method
    p4 = Person(1, 'John Doe', 30, 'USA')
    p5 = Person(2, 'Jane Doe', 25, 'UK')
    p6 = p4 + p5
    print(p6.full_name)  # Output: 'John Doe Jane Doe'
