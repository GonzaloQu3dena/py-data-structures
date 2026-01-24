from typing import Any, Tuple
from circular_linked_list import CircularLinkedList

def exercise_1_traversal_string(cll: CircularLinkedList) -> str:
    """
    Exercise 1: Full Cycle String
    
    Objective:
    Return a string representation of the list.
    Example: "[10] -> [20] -> [30] -> (back to head)"
    
    Logic:
    1. You can use the `__str__` method of the list.
    2. Or iterate using the `for` loop which handles the circularity.
    """
    # TODO: Implement logic
    pass

def exercise_2_find_element(cll: CircularLinkedList, target: Any) -> int:
    """
    Exercise 2: Search in Loop
    
    Objective:
    Find the index of the first occurrence of `target`.
    
    Logic:
    1. Use a `for` loop with an index to iterate over the list.
    2. Compare each element with `target`.
    3. Return the index if found, otherwise -1.
    """
    # TODO: Implement logic
    pass

def exercise_3_sum_all_values(cll: CircularLinkedList) -> int:
    """
    Exercise 3: Summation
    
    Objective:
    Return the sum of all integer values in the circular list.
    
    Logic:
    1. Initialize a `total` variable to 0.
    2. Iterate through the list and add each value.
    3. Return the result.
    """
    # TODO: Implement logic
    pass

def exercise_4_count_nodes(cll: CircularLinkedList) -> int:
    """
    Exercise 4: Size Verification
    
    Objective:
    Manually count the nodes in the list without using `cll.size()`.
    
    Logic:
    1. Start a counter at 0.
    2. Iterate through the list and increment the counter for each node.
    3. Return the count.
    """
    # TODO: Implement logic
    pass

def exercise_5_is_empty_manual(cll: CircularLinkedList) -> bool:
    """
    Exercise 5: Empty Check
    
    Objective:
    Check if the list is empty without using `cll.is_empty()`.
    
    Logic:
    1. Check if `cll.size()` is 0.
    """
    # TODO: Implement logic
    pass

def exercise_6_josephus_survivor(n: int, k: int) -> int:
    """
    Exercise 6: Josephus Problem (Classic)
    
    Objective:
    In a circle of n people, remove every k-th person until only one remains.
    Return the value of the survivor.
    
    Logic:
    1. Create a `CircularLinkedList` and fill it with numbers from 1 to n.
    2. While `cll.size() > 1`:
       a. Rotate the list (move the front to the back) `k - 1` times.
       b. `pop_front()` the k-th element.
    3. Return the last remaining element.
    """
    # TODO: Implement logic
    pass

def exercise_7_rotate_list(cll: CircularLinkedList, times: int) -> None:
    """
    Exercise 7: List Rotation
    
    Objective:
    Shift the starting point of the list `times` positions.
    
    Logic:
    1. For `times` iterations:
       a. `pop_front()` the first element.
       b. `push_back()` that same element.
    """
    # TODO: Implement logic
    pass

def exercise_8_remove_duplicates(cll: CircularLinkedList) -> CircularLinkedList:
    """
    Exercise 8: Deduplicate
    
    Objective:
    Create a new circular list without duplicate values.
    
    Logic:
    1. Create a new `CircularLinkedList` and a `seen` set.
    2. Iterate through the original list.
    3. If element not in `seen`, add it and `push_back` to the new list.
    4. Return the new list.
    """
    # TODO: Implement logic
    pass

def exercise_9_split_list(cll: CircularLinkedList) -> Tuple[CircularLinkedList, CircularLinkedList]:
    """
    Exercise 9: Split in Half
    
    Objective:
    Split one circular list into two separate circular lists.
    
    Logic:
    1. Create two new `CircularLinkedList` objects.
    2. Calculate the middle point (`size() // 2`).
    3. Fill the first list with the first half and the second with the rest.
    4. Return a tuple (list1, list2).
    """
    # TODO: Implement logic
    pass

def exercise_10_concatenate(cll1: CircularLinkedList, cll2: CircularLinkedList) -> CircularLinkedList:
    """
    Exercise 10: Merge Cycles
    
    Objective:
    Merge two circular lists into one single cycle.
    
    Logic:
    1. Create a new `CircularLinkedList`.
    2. Append all elements from `cll1`.
    3. Append all elements from `cll2`.
    4. Return the new list.
    """
    # TODO: Implement logic
    pass