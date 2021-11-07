# Determine if the sum of two integers is equal to the given value
"""
Given an array of integers and a value, determine if there are any two integers in the array whose sum is equal to the given value.
Return true if the sum exists and return false if it does not. Consider this array and the target sums:
"""
def determine_sum(numbers:list,target:int):
    determined_nums=[]
    for number in numbers:
        temp=numbers.copy()
        temp.remove(number)
        if target-number in temp:
            determined_nums.append([number,target-number])
    print(determined_nums)

determine_sum([5,7,1,2,8,4,3],10)

# qa 3 https://www.educative.io/blog/crack-amazon-coding-interview-questions