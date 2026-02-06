"""
File: exercises.py
Purpose: LAB: DOUBLY LINKED LIST CHALLENGES
Author: GonzaloQu3dena
Date: 2026-02-05
Version: 1.1
"""

from typing import Any
from doubly_linked_list import DoublyLinkedList

def exercise_1_forward_traversal_string(dll: DoublyLinkedList) -> str:
    """
    Exercise 1: Forward String
    
    Objective:
    Return a string representation of the list from Head to Tail.
    Example: "10 <-> 20 <-> 30"
    
    Logic:
    1. You can use the `__str__` method of the list or iterate 
       manually using a `for` loop.
    2. Join the elements with " <-> ".
    """
    # TODO: Implement logic
    pass

def exercise_2_backward_traversal_string(dll: DoublyLinkedList) -> str:
    """
    Exercise 2: Backward String
    
    Objective:
    Return a string representation of the list from Tail to Head.
    Example: "30 <-> 20 <-> 10"
    
    Logic:
    1. Use the `backward_iter()` method to traverse from the end.
    2. Collect the values and join them with " <-> ".
    """
    # TODO: Implement logic
    pass

def exercise_3_find_element(dll: DoublyLinkedList, target: Any) -> int:
    """
    Exercise 3: Search
    
    Objective:
    Find the index of the first occurrence of `target`.
    
    Logic:
    1. Iterate through the list using a `for` loop with an index.
    2. Compare each element with `target`.
    3. Return the index if found, otherwise return -1.
    """
    # TODO: Implement logic
    pass

def exercise_4_sum_all_values(dll: DoublyLinkedList) -> int:
    """
    Exercise 4: Summation
    
    Objective:
    Return the sum of all numerical values in the list.
    
    Logic:
    1. Initialize a `total` variable to 0.
    2. Use a `for` loop to iterate over the elements.
    3. Add each element to the total.
    4. Return the result.
    """
    # TODO: Implement logic
    pass

def exercise_5_is_palindrome(dll: DoublyLinkedList) -> bool:
    """
    Exercise 5: Palindrome Check
    
    Objective:
    Check if the list reads the same forwards and backwards.
    
    Logic:
    1. If the list is empty or has one element, return True.
    2. Use two pointers approach:
       a. One starting from index 0.
       b. One starting from index `size() - 1`.
    3. Compare values using `get(i)` and `get(j)`.
    4. Move pointers towards the middle.
    """
    # TODO: Implement logic
    pass

def exercise_6_reverse_inplace(dll: DoublyLinkedList) -> None:
    """
    Exercise 6: Reverse List
    
    Objective:
    Reverse the order of elements in the list.
    
    Logic:
    1. Since we use the public API:
       a. Extract all elements into a temporary list.
       b. Clear the current list (by popping all elements).
       c. Push elements back into the list in the correct order.
    """
    # TODO: Implement logic
    pass

def exercise_7_rotate_right(dll: DoublyLinkedList, k: int) -> None:
    """
    Exercise 7: Rotate List
    
    Objective:
    Move the last `k` elements to the front.
    Example: [1, 2, 3, 4, 5], k=2 -> [4, 5, 1, 2, 3]
    
    Logic:
    1. If the list is empty or `k == 0`, do nothing.
    2. For `k` times:
       a. `pop_back()` the last element.
       b. `push_front()` that element.
    """
    # TODO: Implement logic
    pass

def exercise_8_remove_duplicates(dll: DoublyLinkedList) -> DoublyLinkedList:
    """
    Exercise 8: Deduplicate
    
    Objective:
    Create a new list without duplicate values.
    
    Logic:
    1. Create a new `DoublyLinkedList` and a `seen` set.
    2. Iterate through the original list.
    3. If the element is not in `seen`:
       a. Add it to `seen`.
       b. `push_back()` to the new list.
    4. Return the new list.
    """
    # TODO: Implement logic
    pass

def exercise_9_concatenate(dll1: DoublyLinkedList, dll2: DoublyLinkedList) -> DoublyLinkedList:
    """
    Exercise 9: Merge
    
    Objective:
    Create a new list containing elements of `dll1` followed by `dll2`.
    
    Logic:
    1. Create a new `DoublyLinkedList`.
    2. Append all elements from `dll1`.
    3. Append all elements from `dll2`.
    4. Return the result.
    """
    # TODO: Implement logic
    pass

def exercise_10_kth_from_end(dll: DoublyLinkedList, k: int) -> Any:
    """
    Exercise 10: K-th from End
    
    Objective:
    Return the value of the node that is K positions from the end.
    
    Logic:
    1. Calculate the target index: `size() - k`.
    2. Return `get(target_index)` if valid.
    """
    # TODO: Implement logic
    pass
