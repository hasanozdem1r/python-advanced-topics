"""
User Defined Exception Classes
@Hasan Özdemir 07-10-2022
"""
"""
def validate_username(username:str):
    if len(username)<10:
        raise ValueError

validate_username("hasanozdem1r")
validate_username("hasan")
"""


class NameTooShortError(ValueError):
    pass


def validate_username(username: str):
    if len(username) < 10:
        raise NameTooShortError(username)


validate_username("hasanozdem1r")
validate_username("hasan")
