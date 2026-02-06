"""
File: exercises.py
Purpose: LAB: ONE-DIMENSIONAL ARRAY CHALLENGES
Author: GonzaloQu3dena
Date: 2026-02-05
Version: 1.1
"""

from static_array import StaticArray

def exercise_1_populate_fixed_array():
    """
    Exercise 1: Populate with Pattern
    
    Objective:
    Create a StaticArray of capacity 10 and fill it with the 
    first 10 even numbers (2, 4, 6... 20).
    
    Logic:
    Use a loop and the formula `value = (i + 1) * 2`. 
    This tests your ability to initialize and write to the array.
    """
    # TODO: Implement logic
    pass

def exercise_2_sum_of_elements(arr: StaticArray):
    """
    Exercise 2: Sum of Elements
    
    Objective:
    Iterate through the array and calculate the sum of all 
    integers stored in it. Print the total.
    
    Logic:
    Initialize an accumulator variable to 0 and add each 
    element as you traverse the array.
    """
    # TODO: Implement logic
    pass

def exercise_3_linear_search(arr: StaticArray, target: int):
    """
    Exercise 3: Find Element Index
    
    Objective:
    Find the first occurrence of `target` in the array and 
    print its index. If not found, print -1.
    
    Logic:
    Standard Linear Search: Check elements one by one from 
    index 0 to size-1. Return immediately upon finding a match.
    """
    # TODO: Implement logic
    pass

def exercise_4_find_min_max(arr: StaticArray):
    """
    Exercise 4: Find Min and Max
    
    Objective:
    Find both the minimum and maximum values in the array 
    using a single traversal.
    
    Logic:
    Initialize `min_val` and `max_val` using the first element. 
    Compare every subsequent element against these two variables 
    and update them if necessary.
    """
    # TODO: Implement logic
    pass

def exercise_5_count_occurrences(arr: StaticArray, target: int):
    """
    Exercise 5: Frequency Counter
    
    Objective:
    Count how many times `target` appears in the array.
    
    Logic:
    Different from Linear Search, do not stop at the first match. 
    Traverse the entire array and increment a counter every time 
    `arr[i] == target`.
    """
    # TODO: Implement logic
    pass

def exercise_6_replace_negatives(arr: StaticArray):
    """
    Exercise 6: Conditional Replacement
    
    Objective:
    Replace all negative numbers in the array with 0.
    
    Logic:
    Iterate through the array. If `arr[i] < 0`, use the 
    `set(index, 0)` method to update the value.
    """
    # TODO: Implement logic
    pass

def exercise_7_is_sorted_ascending(arr: StaticArray):
    """
    Exercise 7: Verify Order
    
    Objective:
    Check if the array is sorted in strictly ascending order.
    Return True or False.
    
    Logic:
    Iterate up to `size - 1`. Check if `arr[i] > arr[i+1]`. 
    If this condition is met once, the array is NOT sorted.
    """
    # TODO: Implement logic
    pass

def exercise_8_reverse_in_place(arr: StaticArray):
    """
    Exercise 8: Reverse Array
    
    Objective:
    Reverse the contents of the array without using a second array.
    
    Logic:
    Use the 'Two Pointers' technique. One pointer at start (0), 
    one at end (size-1). Swap values and move pointers inward 
    until they meet.
    """
    # TODO: Implement logic
    pass

def exercise_9_check_palindrome(arr: StaticArray):
    """
    Exercise 9: Palindrome Check
    
    Objective:
    Determine if the array reads the same forwards and backwards 
    (e.g., [1, 2, 3, 2, 1]).
    
    Logic:
    Similar to Reverse, use Two Pointers. Compare `arr[start]` 
    vs `arr[end]`. If they are ever different, it's not a palindrome.
    """
    # TODO: Implement logic
    pass

def exercise_10_remove_duplicates_sorted(arr: StaticArray):
    """
    Exercise 10: Remove Duplicates from Sorted Array
    
    Objective:
    Given a sorted array, remove duplicates in-place so that 
    each element appears only once. Reduce the size accordingly.
    
    Logic:
    Use a `write_index` pointer. Iterate through the array. 
    If the current element is different from the last written 
    element, write it to `write_index` and increment the pointer.
    """
    # TODO: Implement logic
    pass