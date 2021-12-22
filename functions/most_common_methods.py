"""
Most common Python built in methods
@Hasan Ozdemir 2021
"""

"""
Let's assume that we have numbers list [1,2,3,4,5,-1,-2,-3,-4,-5] and we want to convert all to positive numbers.
abs(number) method used for this purpose
"""
numbers = [num for num in range(-5, 6, 1)]
abs_nums = [abs(num) for num in numbers]
print(numbers)
print(abs_nums)

numbers2 = [1.1, 1.2, 1.3, 1.4, 1.5, 1.6, 1.7, 1.8, 1.9]
"""
round(number) is used to round numbers to closes point
NOTE : When there is equality to down and top Python round number to top.
For ex : 1.5 is equal to 1 and 2 and return is 2
"""
rounded_nums = [round(num) for num in numbers2]
print(numbers2)
print(rounded_nums)

"""
all(list) method is used to determine list items are true or false and return the items. 
If all items are true all() returns true if one even is false function return false
"""
print(all(rounded_nums))

"""
any(list) is used to specify is there any True item in a list. 
If even is there 1 item is True method returns True neither returns False 
"""
print(any(rounded_nums))

"""
The repr() function returns the string representation of the value passed to eval function by default
"""
print(repr('Hasan Ozdemir'))

"""
The eval() method parses the expression passed to this method and runs python expression (code) within the program.
eval(expression, globals=None, locals=None)
"""
print(eval('5+25'))
print(eval('12+5+45+75'))

"""
The exec() method executes the dynamically created program, which is either a string or a code object.
exec(object, globals, locals)
"""
# create mka variable during runtime
print(exec('mka="Mustafa Kemal Ataturk"'))
# print mka variable
print(mka)

# The globals() method returns the dictionary of the current global symbol table.
# print(globals())

# The locals() method updates and returns a dictionary of the current local symbol table.
# print(locals())

# https://python-istihza.yazbel.com/gomulu_fonksiyonlar.html#divmod
