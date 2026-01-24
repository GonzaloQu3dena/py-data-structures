"""
File: exercises.py
Purpose: LAB: QUEUE CHALLENGES
Author: GonzaloQu3dena
Date: 2026-01-23
Version: 1.0
"""

from typing import List
from queue import Queue

def exercise_1_reverse_queue(q: Queue) -> None:
    """
    Exercise 1: Queue Reversal
    
    Objective:
    Reverse the elements of a queue using a Stack as auxiliary storage.
    
    Logic:
    1. Create a `Stack` (or use a list as a stack).
    2. While the queue is not empty, `dequeue` elements and `push` them to the stack.
    3. While the stack is not empty, `pop` elements and `enqueue` them back to the queue.
    """
    # TODO: Implement logic
    pass

def exercise_2_generate_binary_numbers(n: int) -> List[str]:
    """
    Exercise 2: Binary Number Generation
    
    Objective:
    Generate binary numbers from 1 to n using a queue.
    Example: n=3 -> ["1", "10", "11"]
    
    Logic:
    1. Create a `Queue` and `enqueue("1")`.
    2. Loop n times:
       a. `dequeue` the current binary string.
       b. Store it in the result list.
       c. `enqueue(current + "0")`.
       d. `enqueue(current + "1")`.
    3. Return the result list.
    """
    # TODO: Implement logic
    pass

def exercise_3_hot_potato_game(names: List[str], num: int) -> str:
    """
    Exercise 3: Hot Potato Simulation
    
    Objective:
    Simulate the "Hot Potato" game where people in a circle pass an item. 
    Every `num` passes, the person holding the potato is eliminated.
    
    Logic:
    1. Enqueue all names into a `Queue`.
    2. While the queue has more than one person:
       a. For `num` times: `enqueue(dequeue())` (move the person to the back).
       b. `dequeue()` the person holding the potato (elimination).
    3. Return the last remaining person.
    """
    # TODO: Implement logic
    pass

def exercise_4_interleave_queue(q: Queue) -> None:
    """
    Exercise 4: Interleave Half of Queue
    
    Objective:
    Interleave the first half of the queue with the second half.
    Example: [1, 2, 3, 4] -> [1, 3, 2, 4]
    
    Logic:
    1. Use a temporary storage (like a stack or another queue) to hold the first half.
    2. Rearrange the elements so they alternate.
    """
    # TODO: Implement logic
    pass

def exercise_5_is_palindrome_queue(text: str) -> bool:
    """
    Exercise 5: Palindrome Check (Queue & Stack)
    
    Objective:
    Check if a string is a palindrome by comparing a Queue (FIFO) and a Stack (LIFO).
    
    Logic:
    1. Push all characters into a `Stack` and enqueue them into a `Queue`.
    2. Compare elements one by one. If they all match, it's a palindrome.
    """
    # TODO: Implement logic
    pass

def exercise_6_first_non_repeating(stream: str) -> str:
    """
    Exercise 6: First Non-Repeating Character
    
    Objective:
    Find the first non-repeating character in a stream of characters.
    
    Logic:
    1. Use a `Queue` to store the order of characters and a dictionary to count frequencies.
    2. For each character:
       a. Increment count.
       b. Enqueue character.
       c. While queue front is a repeating character, dequeue it.
    """
    # TODO: Implement logic
    pass

def exercise_7_implement_stack_using_queues() -> None:
    """
    Exercise 7: Stack with Queues
    
    Objective:
    Implement a Stack (LIFO) using two Queues (FIFO).
    
    Logic:
    1. To `push`, enqueue to the active queue.
    2. To `pop`, move all elements except the last one to the second queue, 
       then dequeue the last one.
    """
    # TODO: Implement logic
    pass

def exercise_8_circular_buffer_simulation(size: int) -> None:
    """
    Exercise 8: Circular Buffer
    
    Objective:
    Simulate a fixed-size buffer where new data overwrites the oldest data if full.
    
    Logic:
    1. Use a `Queue`. Before enqueuing, check if `size()` == `limit`.
    2. If full, `dequeue()` before adding the new item.
    """
    # TODO: Implement logic
    pass

def exercise_9_level_order_traversal_simulation() -> None:
    """
    Exercise 9: Level Order Concept
    
    Objective:
    Explain how a queue is used to visit all nodes of a tree level by level.
    
    Logic:
    1. Enqueue the root.
    2. While queue is not empty:
       a. `dequeue` current node.
       b. Enqueue its children (left, then right).
    """
    # TODO: Implement logic
    pass

def exercise_10_emergency_room_simulation() -> None:
    """
    Exercise 10: Simple ER Queue
    
    Objective:
    Simulate an Emergency Room where patients are served in order.
    """
    # TODO: Implement logic
    pass
