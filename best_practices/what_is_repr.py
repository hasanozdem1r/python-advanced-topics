"""
This script summarize repr method
@Hasan Ozdemir 05-13-2022
"""


class Tractor:

    def __init__(self, horse_power: int, model: int, cylinder: int, km: int):
        self.horse_power = horse_power
        self.model = model
        self.cylinder = cylinder
        self.km = km

    def __str__(self):
        return f"{self.horse_power} - {self.model} - {self.cylinder} - {self.km}"

    def __repr__(self):
        return f"{self.horse_power} - {self.model} - {self.cylinder} - {self.km}"


if __name__ == "__main__":
    fiat_obj = Tractor(horse_power=64, model=1982, cylinder=3, km=1000)
    print(fiat_obj)
