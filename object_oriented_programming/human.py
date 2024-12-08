from abc import ABC, abstractmethod
from uuid import uuid4
class Human(ABC):

    def __init__(self,person_id:str,birthdate:int,kilo:float,height:int):
        super().__init__()
        self.person_id = person_id
        self.birthdate=birthdate
        self.kilo = kilo
        self.height = height

    def __str__(self):
        return super().__str__()
    
    def __repr__(self):
        return super().__repr__()
    
    def get_information(self):
        return f'ID: {self.person_id}\nBirthdate: {self.birthdate}\nKilo: {self.kilo}\nHeight: {self.height}'
    

class Person(Human):

    def __init__(self, person_id, birthdate, kilo, height,full_name,nation):
        super().__init__(person_id, birthdate, kilo, height)
        self.full_name = full_name
        self.nation = nation

    def __str__(self):
        return f'Person ID:{self.person_id}'
    
    def __repr__(self):
        return f'Full Name: {self.full_name}'

    def get_information(self):
        return f'ID: {self.person_id}\nFull Name: {self.full_name}\nBirthdate: {self.birthdate}\nKilo: {self.kilo}\nHeight: {self.height}'

if __name__ == "__main__":
    p1 = Person(
        person_id=str(uuid4()),
        birthdate=1997,
        kilo=95.0,
        height=183,
        full_name="Hasan Ozdemir",
        nation="Turkiye"
    )