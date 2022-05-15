"""
Python script to understand fundamentals of ZIP function

@ Hasan Ozdemir 2021
"""

# while .. else in practice -> evaluating stack programs
def is_comment(item):
    return isinstance(item, str) and item.startswith("#")


def execute(program):
    """
    Execute a stack program
    :param program: Any stack-like containing where each item in the stack is a callable
    operators or non-callable operands. The top-most items on the stack may be strings beginning
    with '#' for the purposes of documentation. Stack-like means support for :
    item=stack.pop() #remove and return the top item
    stack.append(item) #push and item to the top
    if stack : false in a boolean contact when empty
    :return:
    """
    # Find the start of the 'program' by skipping
    # any item which is a comment
    while program:
        item = program.pop()
        if not is_comment(item):
            program.append(item)
            break
        else:  # no break
            print("Empty program")
            return
        # Evaluate the program
        pending = []
        while program:
            item = program.pop()
            if callable(item):
                try:
                    result = item(*pending)
                except Exception as e:
                    print("Error", e)
                    break
                program.append(result)
                pending.clear()
            else:
                pending.append(item)
        else:  # no break
            print("Program successfull")
            print("Result", pending)
        print("Finished")


if __name__ == "__main__":
    import operator

    program = list(
        reversed(
            (
                "#A short stack program to add",
                " and multiply some constants",
                5,
                2,
                operator.add,
                3,
                operator.mul,
            )
        )
    )
    execute(program)
