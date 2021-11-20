# is a string balanced
# balanced -> {} squiggles , [] brackets, () parenthesis
class Brackets:

    def balanced_brackets(self,characters:str)->bool:
        punctuation_stack=[]
        # keys ---> (, {, [
        # values -> ), }, ]
        tokens={'(':')','{':'}','[':']'}
        punctuations = ['[', ']', '(', ')', '{', '}']
        for char in characters:
            if char in punctuations:
                punctuation_stack.append(char)
            if len(punctuation_stack)>1 and punctuation_stack[-2] in tokens.keys():
                if punctuation_stack[-1]==tokens[punctuation_stack[-2]]:
                    punctuation_stack.remove(punctuation_stack[-1])
                    punctuation_stack.remove(punctuation_stack[-1])

        return True if len(punctuation_stack)==0 else False

if __name__ == '__main__':
    test_obj=Brackets()
    print(test_obj.balanced_brackets('('))
    # [()]{}{[()()]()} -> True
    print(test_obj.balanced_brackets('[()]{}{[()()]()}'))
    # {{[[(())]]}}  -> True
    print(test_obj.balanced_brackets('{{[[(())]]}}'))
    # }([]]][[){}}[[)}[(}(}]{(}[{}][{}](}]}))]{][[}(({(]}[]{[{){{(}}[){[][{[]{[}}[)]}}]{}}(} NO
    print(test_obj.balanced_brackets('}([]]][[){}}[[)}[(}(}]{(}[{}][{}](}]}))]{][[}(({(]}[]{[{){{(}}[){[][{[]{[}}[)]}}]{}}(}'))
"""
( -> ( 
([ -> ([
([] -> (
(] -> (]
(]( -> (](
(]() -> (] 
"""
"""
([])
"""