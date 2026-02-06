"""
File: exercises.py
Purpose: LAB: STACK CHALLENGES
Author: GonzaloQu3dena
Date: 2026-02-05
Version: 1.1
"""

from typing import Any, List
from stack import Stack

def exercise_1_reverse_string(text: str) -> str:
    """
    Exercise 1: String Reversal
    
    Objective:
    Use a stack to reverse a given string.
    
    Logic:
    1. Create a `Stack` of characters.
    2. Iterate through the string and `push` each character into the stack.
    3. Pop each character from the stack and append it to a new string.
    4. Return the reversed string.
    """
    # TODO: Implement logic
    pass

def exercise_2_balanced_parentheses(expression: str) -> bool:
    """
    Exercise 2: Balanced Parentheses
    
    Objective:
    Check if the parentheses in a string are correctly balanced (e.g., "(())" is True).
    
    Logic:
    1. Create a `Stack`.
    2. Iterate through each character:
       a. If it's '(', `push` it.
       b. If it's ')', `pop` from the stack. 
    3. If you try to pop from an empty stack, it's unbalanced.
    4. After the loop, the stack must be empty.
    """
    # TODO: Implement logic
    pass

def exercise_3_decimal_to_binary(number: int) -> str:
    """
    Exercise 3: Number Base Conversion
    
    Objective:
    Convert a positive integer to its binary representation using a stack.
    
    Logic:
    1. Create a `Stack`.
    2. While the number > 0:
       a. `push` the remainder of `number % 2` to the stack.
       b. Update `number = number // 2`.
    3. Pop all elements from the stack to form the binary string.
    """
    # TODO: Implement logic
    pass

def exercise_4_reverse_list(items: List[Any]) -> List[Any]:
    """
    Exercise 4: List Reversal
    
    Objective:
    Reverse the order of elements in a list using a stack.
    
    Logic:
    1. Push all elements of the list into a `Stack`.
    2. Pop them one by one and put them back into a new list.
    """
    # TODO: Implement logic
    pass

def exercise_5_is_palindrome(text: str) -> bool:
    """
    Exercise 5: Palindrome Check
    
    Objective:
    Determine if a string is a palindrome using a stack.
    
    Logic:
    1. Push all characters into a stack.
    2. Compare the string characters one by one with the elements popped from the stack.
    """
    # TODO: Implement logic
    pass

def exercise_6_sort_stack(stack: Stack[int]) -> Stack[int]:
    """
    Exercise 6: Sort a Stack
    
    Objective:
    Sort a stack so that the smallest elements are on top, using only another temporary stack.
    
    Logic:
    1. Create a `temp_stack`.
    2. While the original stack is not empty:
       a. Pop an element `tmp`.
       b. While `temp_stack` is not empty and `temp_stack.peek() > tmp`:
          - Pop from `temp_stack` and push back to original stack.
       c. Push `tmp` to `temp_stack`.
    3. Return `temp_stack`.
    """
    # TODO: Implement logic
    pass

def exercise_7_backspace_compare(s: str, t: str) -> bool:
    """
    Exercise 7: Backspace String Compare
    
    Objective:
    Given two strings with '#' representing a backspace, determine if they are equal.
    
    Logic:
    1. Process both strings using two separate stacks.
    2. For each character:
       a. If not '#', push it.
       b. If '#', pop from stack (if not empty).
    3. Compare the resulting stacks.
    """
    # TODO: Implement logic
    pass

def exercise_8_evaluate_postfix(expression: str) -> int:
    """
    Exercise 8: Postfix Evaluation (RPN)
    
    Objective:
    Evaluate a mathematical expression in Postfix notation (e.g., "5 3 +" -> 8).
    
    Logic:
    1. Use a stack to store numbers.
    2. Iterate through the expression:
       a. If it's a number, push it.
       b. If it's an operator: pop two operands, apply operator, push result.
    """
    # TODO: Implement logic
    pass

def exercise_9_min_stack_logic() -> None:
    """
    Exercise 9: Min Stack Concept
    
    Objective:
    Design a stack that retrieves the minimum element in O(1) time.
    
    Logic:
    1. Use two internal `Stack` objects: one for data, one for minimums.
    2. When pushing X, also push `min(X, current_min)` to the min_stack.
    """
    # TODO: Implement logic
    pass

def exercise_10_undo_redo_logic() -> None:
    """
    Exercise 10: Undo/Redo Simulation
    
    Objective:
    Simulate a text editor's undo and redo functionality using two stacks.
    """
    # TODO: Implement logic
    pass