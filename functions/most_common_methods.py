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

"""
The divmod(number1,number2) method return tuple(n1/n2,n1%n2) 
Method returns result of division and reminder of division
"""
print(divmod(10, 2))  # expected (5,0)
print(divmod(10, 3))  # expected (3,1)

"""
The enumerate(iterable,start_index) method adds a counter to an iterable and returns it in a form of enumerating object.
"""
for index, item in enumerate('Hasan Özdemir'):
    print(index, item)
print(list(enumerate('Ankara')))

"""
The id(object) method return the unique id of given object. The identity of every object in Python is unique.
"""
h='Turkey'
a='Poland'
print(id(h)==id(h))
print(id(a)==id(a))
print(id(a)==id(h))

"""
The format(object) method is used to format the given data.
"""
print(format(12,".2f"))
print('{:.2f}'.format(12))
"""
The filter() method filters the given sequence with the help of a function that tests each element in the sequence to be true or not.
"""
notes = {'Ahmet'   : 60,
          'Sinan'   : 50,
          'Mehmet'  : 45,
          'Ceren'   : 87,
          'Selen'   : 99,
          'Cem'     : 98,
          'Can'     : 51,
          'Kezban'  : 100,
          'Hakan'   : 66,
          'Mahmut'  : 80}
def filter_note(note):
    return note >= 70

print(*filter(filter_note,notes.values()))
"""
The hash(object) method returns the hash value of an object if it has one. 
Hash values are just integers that are used to compare dictionary keys during a dictionary look quickly.
"""
text="Fucking Covid 19"
print(hash(text))
"""
The isinstance(object) method used to type check. Return True or False
"""
print(isinstance('Hasan',str)) # True
print(isinstance("Atatürk",bool)) # False
"""
The len(object) is used to check length of string, collections and more
"""
print(len(notes))
"""
The map(function, iterable, ...) function applies a given function to each item of an iterable (list, tuple etc.) and returns an iterator.
"""
def square(num):
    return num**2
squared_iterator=map(square,[i for i in range(1,11)])
squared_list=list(squared_iterator)
print(squared_list)

"""
The max(object) returns maximum item from the list.
"""
print(max([i for i in range(1000,1,-1)]))

"""
The min(object) returns minimum item from the list.
"""
print(min([i for i in range(1000,1,-1)]))

"""
The pow(object1,object2) returns the power of the base. It's work like base**power 
"""
print(pow(4,2))

"""
The reversed(object) method reverse the given list
"""
names = ['ahmet', 'mehmet', 'veli', 'ayşe', 'çiğdem', 'ışık']
print(list(reversed(names)))
print(names[::-1]==list(reversed(names)))

"""
The sorted(object) sort the list with specific conditions
"""
print(sorted('Hasan')) # sorted regarding to character position in list
print(sorted([i for i in range(10)]))