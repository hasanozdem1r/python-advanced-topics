"""
You are given an array of positive numbers from 1 to n, such that all numbers from 1 to n are present except one number x.
You have to find x. The input array is not sorted.
Look at the below array and give it a try before checking the solution.
"""
def find_missing_number(numbers:list):
    actual_sum=sum(numbers)
    # there is only 1 number missing
    size=len(numbers)+1
    expected_sum=(size*(size+1))/2
    print(int(expected_sum-actual_sum))

find_missing_number([1,2,3,5,]) 