class Person:

    def __init__(self, person_id, full_name, age, country_of_residence) -> None:
        self.person_id = person_id
        self.full_name = full_name
        self.age = age
        self.country_of_residence = country_of_residence

    def __str__(self) -> str:
        return f"Full-name:{self.full_name} - Age:{self.age} - Country of Residence:{self.country_of_residence}"


if __name__ == "__main__":
    p1 = Person(person_id=1,
                full_name="Hasan Ozdemir",
                age=25,
                country_of_residence="Türkiye")
    # call __str__ method
    print(p1)
