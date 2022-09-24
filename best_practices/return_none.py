"""
This script is aiming to show how to return nothing / None in Python
@Hasan Ozdemir 05-13-2022
"""


# below all methods return the same thing
def none_1() -> None:
    name = "Hasan"
    surname = "Ozdemir"


def none_2() -> None:
    name = "Hasan"
    surname = "Ozdemir"
    return None


def none_3() -> None:
    """Bare return statement implies `return None`"""
    name = "Hasan"
    surname = "Ozdemir"
    return None


def none_4(value) -> str:
    """Missing return statement implies `return None`"""
    if value:
        return "x"


"""
All three functions properly return None
if you pass them a falsy value as the sole argument
"""
print(none_1(), none_2(), none_3(), none_4(value=""))
