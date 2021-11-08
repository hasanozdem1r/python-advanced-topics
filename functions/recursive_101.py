# typical user defined function
def find_factorial(number):
    result=1
    for num in range(number,1,-1):
        result=result*num
    print(result)

find_factorial(5)

def find_factorial_recursive(number):
    if number==0:
        return 1
    return number*find_factorial_recursive(number-1)
print(find_factorial_recursive(5))