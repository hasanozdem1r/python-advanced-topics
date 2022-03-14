from test_data import lotto_numbers, random_numbers, sorted_numbers
from math import sqrt


class Search:
    def __init__(self):
        pass

    def linear_search(self, target_value: int, numbers: list):
        """
        The time complexity of linear search is O(n)
        Linear search is a good fit for when we need to find the first occurrence of an item in an unsorted collection because unlike most other search algorithms,
        it does not require that a collection be sorted before searching begins.
        :param target_value: <int> number to be searched
        :param numbers: <list> numbers list
        :return: <bool> True -> Element found, False -> Element not found
        """
        for item in numbers:
            if target_value == item:
                return True
        return False

    def binary_search(self, target_value: int, numbers: list):
        """
        Binary search follows a divide and conquer methodology
        It is faster than linear search but requires that the array be sorted before the algorithm is executed.
        :param target_value: <int> number to be searched
        :param numbers: <list> sorted numbers list
        :return: <bool> True -> Element found, False -> Element not found
        """
        first_index: int = 0
        last_index: int = len(numbers) - 1
        while first_index <= last_index:
            middle_index: int = (first_index + last_index) // 2
            if numbers[middle_index] == target_value:
                return True
            else:
                if numbers[middle_index] > target_value:
                    last_index = middle_index - 1
                else:
                    first_index = middle_index + 1
        return False

    def jump_search(self, target_value: int, numbers: list):
        """
        Jump search works on a sorted array, and uses a similar divide and conquer approach to search through it.
        It can be classified as an improvement of the linear search algorithm since
        it depends on linear search to perform the actual comparison when searching for a value.
        The time complexity of jump search is O(?n), where ?n is the jump size, and n is the length of the list,
        placing jump search between the linear search and binary search algorithms in terms of efficiency.
        :param target_value: <int> number to be searched
        :param numbers: <list> numbers list
        :return: <bool> True -> Element found, False -> Element not found
        """
        length = len(numbers)
        jump_step: int = int(sqrt(length))
        left, right = 0, 0
        while left < length and numbers[left] < target_value:
            right = min(length - 1, left + jump_step)
            if numbers[left] <= target_value and numbers[right] >= target_value:
                break
            left += jump_step
        if left >= length or numbers[left] > target_value:
            return False
        right = min(length - 1, right)
        i = left
        while i <= right and numbers[i] <= target_value:
            if numbers[i] == target_value:
                return True
            i += 1
        return False


search_obj = Search()
print(search_obj.linear_search(12, random_numbers))

print(search_obj.binary_search(12, sorted_numbers))

print(search_obj.jump_search(2121, sorted_numbers))

# https://stackabuse.com/search-algorithms-in-python/
