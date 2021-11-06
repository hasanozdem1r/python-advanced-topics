"""
Find the number of * between | |
Input :
|***********||||||||||*|||*********
Output : 11 + 1
"""

def method_1(text:str):
    opener=0
    star=0
    for i in text:
        if i=='|':
            opener+=1
        elif opener==1:
            star+=1
        elif opener==2:
            opener=0
    print(star)

method_1("|***********||||||||||*|||*********")