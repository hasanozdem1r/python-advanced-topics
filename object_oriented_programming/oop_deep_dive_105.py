class Vehicle:
    def __init__(self, model, brand):
        self.model = model
        self.brand = brand
        self.number_of_door = 0


class SedanCar(Vehicle):
    def __init__(self):
        super(SedanCar, self).__init__()
        self.number_of_door = 4


class CoupeCar(Vehicle):
    def __init__(self):
        # super(CoupeCar, self).__init__()
        super().__init__()
        self.number_of_door = 2


vehicle = Vehicle(2021, "AUDI")
coupe = CoupeCar()
sedan = SedanCar()
# print(sedan.brand)
print(coupe.brand)
