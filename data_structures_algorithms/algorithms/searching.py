"""
The algorithm consists of iterating over an array and returning the index of the first occurrence of an item once it is found:
"""
from test_data import lotto_numbers,random_numbers,sorted_numbers

class Search:

    def __init__(self):
        pass

    def linear_search(self,target_value:int,target:list):
        """
        The time complexity of linear search is O(n)
        Linear search is a good fit for when we need to find the first occurrence of an item in an unsorted collection because unlike most other search algorithms,
        it does not require that a collection be sorted before searching begins.
        :return: <bool> True -> Element found, False -> Element not found
        """
        for item in target:
            if target_value==item:
                return True
        return False

    def binary_search(self,target_value:int,target:list):
        """
        Binary search follows a divide and conquer methodology
        It is faster than linear search but requires that the array be sorted before the algorithm is executed.
        :return: <bool> True -> Element found, False -> Element not found
        """
        first_index:int=0
        last_index:int=len(target)-1
        while first_index<=last_index:
            middle_index: int = (first_index+last_index) // 2
            if target[middle_index]==target_value:
                return True
            else:
                if target[middle_index]>target_value:
                    last_index=middle_index-1
                else:
                    first_index=middle_index+1
        return False




search_obj=Search()
print(search_obj.linear_search(12,random_numbers))

print(search_obj.binary_search(12,sorted_numbers))