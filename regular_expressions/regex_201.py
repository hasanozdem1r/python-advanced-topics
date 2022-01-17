"""
This script is created to teach fundamental of metacharacters at RegEx
@Hasan Özdemir 01/17/2022
"""
import re

create_star = lambda: print("*" * 50)

name_list = ["özcan", "mehmet", "süleyman", "selim", "kemal", "özkan", "esra", "dündar", "esin", "esma", "özhan",
             "özlem"]

# [] Brackets metacharacter : Refer set of characters
# [chk]
check_match = lambda item: re.search('öz[chk]an', item)
matches = [check_match(item).group() for item in name_list if check_match(item)]
print(matches)

create_star()
# [0-9][A-Z]
numbers = ["23BH56", "TY76Z", "4Y7UZ", "TYUDZ", "34Y34", "12345"]
for number in numbers:
    if re.match('[0-9][A-Z]', number):
        print(number)

create_star()
# . Dot metacharacter : Refer any character except new line for on
# e time occurrence
for number in numbers:
    if re.match('..Y', number):
        print(number)
