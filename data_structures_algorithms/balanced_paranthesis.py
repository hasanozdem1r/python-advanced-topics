# is a string balanced
# balanced -> {} squiqles , [] brackets, () parenthesis

def is_balanced(text:str)->bool:
    punctuation=[]
    tokens=['[',']','(',')','{','}']
    for i in text:
        if i in tokens:
            punctuation.append(i)
    if (punctuation.count('(')==punctuation.count(')') and punctuation.count('[')==punctuation.count(']') and punctuation.count('{')==punctuation.count('}')):
        return True
    else:
        return False

print(is_balanced('('))

