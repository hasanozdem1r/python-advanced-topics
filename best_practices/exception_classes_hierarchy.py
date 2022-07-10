"""
User Defined Exception Classes Hierarchy
@Hasan Özdemir 07-10-2022
"""


class BaseValidationError(ValueError):  # Exceptions
    pass


class NameTooShortError(BaseValidationError):  # X Exception
    pass


class NameTooLongError(BaseValidationError):  # Y Exception
    pass


class NameTooCuteError(BaseValidationError):  # Z Exception
    pass


"""
All this exceptions are user defined.
NameTooLongError, NameTooShortError, NameTooCuteError are derived from BaseValidationError so because of that 
BaseValidationError act like Exception class. Catch all errors.
"""



