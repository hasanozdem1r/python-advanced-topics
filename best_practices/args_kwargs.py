"""
This script is aimed to show usage of args and kwargs
@Hasan Ozdemir 05-13-2022
"""


# args : positional arguments
# kwargs: keyword arguments
def args_kwargs_101(required: str, *args, **kwargs) -> None:
    """
    This method aiming to show basics of args and kwargs
    """
    print(required)
    if args:
        # tuple
        print(args)
    if kwargs:
        # dictionary
        print(kwargs)
    kwargs["name"] = "Hasan"
    new_args = args + ("extra",)
    args_kwargs_102(12, *new_args, **kwargs)
    print("*" * 25)


# Forwarding Optional or Keyword Arguments
def args_kwargs_102(x: int, *args, **kwargs):
    if args:
        print(args)
    if kwargs:
        print(kwargs)
    print(x)


if __name__ == "__main__":
    args_kwargs_101(required="Hello")
    # only with args
    args_kwargs_101("Hello 1", 1, 2, 3, 4, 5)
    args_kwargs_101("Hello 2", 1, 2, 3, 4, 5, 6, 7, 8, 9, 0)
    # only with kwargs
    args_kwargs_101("Hello 3", a=1, b=2)
    # with args and kwargs
    args_kwargs_101("Hello 4", 1, 2, 3, 4, key=1, key2=2, key3=3)
