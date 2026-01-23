from singly_linked_list import SinglyLinkedList

def exercise_1_count_occurrences(linked_list: SinglyLinkedList, value: int) -> int:
    """
    Exercise 1: Counter
    
    Objective:
    Count how many times 'value' appears in the list.
    
    Logic:
    1. Initialize a counter to 0.
    2. Iterate through the list using a loop (or the list's iterator).
    3. If the current element matches 'value', increment the counter.
    4. Return the total count.
    
    Example: 1 -> 2 -> 1 -> 3. count(1) returns 2.
    """
    # TODO: Implement logic
    pass

def exercise_2_get_last_element(linked_list: SinglyLinkedList):
    """
    Exercise 2: Find Tail
    
    Objective:
    Return the value of the LAST node.
    
    Logic:
    1. Use `linked_list.size()` to get the length.
    2. If the size is 0, return None.
    3. Use `linked_list.get(index)` to retrieve the element at `size - 1`.
    """
    # TODO: Implement logic
    pass

def exercise_3_sum_all_values(linked_list: SinglyLinkedList) -> int:
    """
    Exercise 3: Summation
    
    Objective:
    Return the sum of all integer values in the list.
    
    Logic:
    1. Initialize `total_sum` to 0.
    2. Iterate through the list (using a `for` loop or `get` in a loop).
    3. Add each value to `total_sum`.
    4. Return the final sum.
    """
    # TODO: Implement logic
    pass

def exercise_4_find_min_max(linked_list: SinglyLinkedList):
    """
    Exercise 4: Min/Max
    
    Objective:
    Return a tuple (min_val, max_val) found in the list.
    
    Logic:
    1. If the list is empty (`size() == 0`), return (None, None).
    2. Initialize `min_val` and `max_val` with the first element (`get(0)`).
    3. Iterate through the rest of the list.
    4. Update `min_val` and `max_val` accordingly.
    5. Return the tuple.
    """
    # TODO: Implement logic
    pass

def exercise_5_concatenate_lists(list1: SinglyLinkedList, list2: SinglyLinkedList) -> SinglyLinkedList:
    """
    Exercise 5: Merge/Concatenate
    
    Objective:
    Create a NEW SinglyLinkedList that contains all elements of list1 followed by list2.
    
    Logic:
    1. Instantiate a new `SinglyLinkedList`.
    2. Iterate through `list1` and `push_back` its elements into the new list.
    3. Iterate through `list2` and `push_back` its elements into the new list.
    4. Return the new list.
    
    Example: L1=[1,2], L2=[3,4] -> Result=[1,2,3,4]
    """
    # TODO: Implement logic
    pass

def exercise_6_reverse_list_inplace(linked_list: SinglyLinkedList):
    """
    Exercise 6: Reverse (Classic Interview Question)
    
    Objective:
    Reverse the order of elements in the list.
    
    Logic:
    1. Since we use the public API, one way is to:
       a. Extract all elements into a temporary storage.
       b. Clear the current list (or just overwrite it).
       c. `push_front` each element back into the list.
    2. Alternatively, use `pop_front()` and `push_front()` logic 
       to reverse the sequence in a new or the same list.
    
    Example: 1 -> 2 -> 3 -> None BECOMES 3 -> 2 -> 1 -> None
    """
    # TODO: Implement logic
    pass

def exercise_7_remove_duplicates(linked_list: SinglyLinkedList):
    """
    Exercise 7: Deduplicate
    
    Objective:
    Remove duplicate values from the list, keeping the first occurrence.
    
    Logic:
    1. Create a NEW `SinglyLinkedList` and a `seen` set.
    2. Iterate through the original list.
    3. For each value, if it's not in `seen`, `push_back` to the new list and add to `seen`.
    4. (Optional) Replace the contents of the original list or return the new one.
    """
    # TODO: Implement logic
    pass

def exercise_8_find_middle_node(linked_list: SinglyLinkedList):
    """
    Exercise 8: The Middle Element
    
    Objective:
    Return the value of the node exactly in the middle.
    
    Logic:
    1. Calculate the middle index using `linked_list.size() // 2`.
    2. Use `linked_list.get(mid_index)` to retrieve and return the value.
    """
    # TODO: Implement logic
    pass

def exercise_9_has_cycle(linked_list: SinglyLinkedList) -> bool:
    """
    Exercise 9: Cycle Detection
    
    Objective:
    Check if the list has a loop.
    
    Logic:
    1. Using the public API, a cycle would make `size()` or `get()` fail 
       or loop infinitely if they don't use the `_size` counter.
    2. In this implementation, `_size` protects us, but a cycle is 
       still possible if nodes are linked manually.
    3. To detect it with the API, track visited indices or values if unique.
    """
    # TODO: Implement logic
    pass

def exercise_10_kth_from_end(linked_list: SinglyLinkedList, k: int):
    """
    Exercise 10: K-th Element from End
    
    Objective:
    Return the value of the node that is K positions from the end.
    
    Logic:
    1. Calculate the target index: `target = size() - k`.
    2. If the index is valid, use `get(target)` to return the value.
    """
    # TODO: Implement logic
    pass
