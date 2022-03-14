"""
Find the number of * between | |
Input :
|***********||||||||||*|||*********
Output : 11 + 1
"""


def count_stars(text: str):
    opener = 0
    star_actual = 0
    stack_star = []
    for i in text:
        stack_star.append(i)
        if stack_star.count("|") == 2:
            stack_star.remove("|")
            stack_star.remove("|")
            star_actual += stack_star.count("*")
            stack_star = ["|"]
    print(star_actual)


count_stars("|***********||||||||||*|||****|*|****")
