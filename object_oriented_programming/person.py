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
