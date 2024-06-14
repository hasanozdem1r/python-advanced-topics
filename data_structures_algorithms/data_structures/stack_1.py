from typing import List
# v1
# create stack from built-in function


class Stack:

    def __init__(self,items:List,capacity:int)->None:
        self.stack = items
        self.capacity = capacity

    def __repr__(self):
        return f"{self.stack}"
    
    def push(self,item):
        if len(self.stack)<self.capacity:
            self.stack.append(item)
            return self.stack
        raise ValueError("Stack capacity is exceed!")

    def pop(self):
        if len(self.stack)>0:
            self.stack.pop()
            return self.stack
        raise ValueError("Stack len is 0!")

    
if __name__ == "__main__":
    stack = Stack([1,2,3,4,5,6,7],100)
    for i in range(8,11):
        stack.push(i)
        print(stack)
    for i in range(60):
        stack.pop()
        print(stack)
    
