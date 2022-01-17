"""
This script is created to teach fundamental of metacharacters at RegEx
@Hasan Özdemir 01/17/2022
"""
import re
from os import listdir, getcwd

create_star = lambda: print("*" * 50)

name_list = ["özcan", "mehmet", "süleyman", "selim", "kemal", "özkan", "esra", "dündar", "esin", "esma", "özhan",
             "özlem"]

# [] Brackets metacharacter : Refer set of characters
# [chk]
check_match = lambda item: re.search('öz[chk]an', item)  # must be one of the letter from the group (c,h,k)
matches = [check_match(item).group() for item in name_list if check_match(item)]
print(matches)

create_star()
# [0-9][A-Z]
numbers = ["23BH56", "TY76Z", "4Y7UZ", "TYUDZ", "34Y34", "12345"]
for number in numbers:
    if re.match('[0-9][A-Z]', number):  # there must be 1 number and 1 uppercase letter minimum
        print(number)

create_star()
# . Dot metacharacter : Refer any character except new line for on
# e time occurrence
for number in numbers:
    if re.match('..Y', number):  # we referred there must be exactly 2 letter before Y
        print(number)

create_star()
# * Star metacharacter : Refer item 0 or more occurrences
list2 = ["st", "sat", "saat", "saaat", "falanca"]
for i in list2:
    if re.match('sa*t', i):  # we referred a letter can repeat 0 or more times
        print(i)

create_star()
# get all .py files from the current folder


index = listdir(getcwd())
for i in index:
    if re.match('.*py', i):
        print(i)

create_star()
# + (plus) metacharacter : One or more occurrences
name_list2 = ["ahmet", "mehmet", "met", "kezban"]
for i in name_list2:
    if re.match('.+met', i):
        print(i)

create_star()
# ? (question mark) : Zero or one occurrence
for i in list2:
    if re.match('sa?t', i):
        print(i)

create_star()
# {} (braces) metacharacter : Exactly the specified number of occurrences
for i in list2:
    if re.match('sa{3}t', i):
        print(i)

create_star()
# ^ metacharacter : It's used to check first index of given string (starts with)
for n in numbers:
    if re.search("^[A-Z]+[0-9]", n):  # we referred any words starts with at uppercase and number6
        print(re.search("^[A-Z]+[0-9]", n).group())

create_star()
# $ (dollar) metacharacter : It's used to check last index of given string (ends with)
list3 = liste = ["at", "katkı", "fakat", "atkı", "rahat", "mat", "yat", "sat", "satılık", "katılım"]
for i in list3:
    if re.search('at$', i):  # we referred any words finish with at
        print(i)

create_star()
# \ (slash) metacharacter : Signals of sequence (also escape character)
list4=["10$", "25€", "20$", "10TL", "25£"]
for i in list4:
    if re.match("[0-9]+\$",i):
        print(i)

create_star()
# | metacharacter : It's used to match more than one pattern
for i in list3:
    if re.search("^at|at$",i):
        print(i)