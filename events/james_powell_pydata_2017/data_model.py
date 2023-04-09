# data model methods
# some behaviour that I want to implement -> __ function __
# top level function or top level syntax -> corresponding __
class Polynomial:

    def __init__(self, *coeffs) -> None:
        self.coeffs = coeffs

    # repr(p1) better output
    def __repr__(self) -> str:
        return 'Polynomial(*{!r})'.format(self.coeffs)

    def __add__(self, other):
        return Polynomial(*(x + y for x, y in zip(self.coeffs, other.coeffs)))

    def __len__(self):
        return len(self.coeffs)


if __name__ == "__main__":
    # python -i events/james_powell_pydata_2017/data_model.py # run interactive
    p1 = Polynomial(1, 2, 3)  # x²+2x+3
    p2 = Polynomial(3, 4, 3)  # 3x²+4x+3
