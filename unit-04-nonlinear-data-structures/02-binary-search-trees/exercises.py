"""
File: exercises.py
Purpose: LAB: BINARY SEARCH TREE CHALLENGES
Author: GonzaloQu3dena
Date: 2026-02-05
Version: 1.1
"""

from typing import Any, List, Optional
from binary_search_tree import BinarySearchTree

def exercise_1_count_all_nodes(bst: BinarySearchTree) -> int:
    """
    Exercise 1: Node Counter
    
    Objective:
    Count the total number of nodes in the BST.
    
    Logic:
    Use the inorder traversal to get all elements and return the length of the result list.
    """
    # TODO: Implement logic
    pass

def exercise_2_find_max_value(bst: BinarySearchTree) -> Optional[int]:
    """
    Exercise 2: Peak Finder
    
    Objective:
    Find the maximum value stored in an integer BST.
    
    Logic:
    Since it's a BST, the inorder traversal returns sorted values. 
    The maximum value will be the last element of the list.
    """
    # TODO: Implement logic
    pass

def exercise_3_find_min_value(bst: BinarySearchTree) -> Optional[int]:
    """
    Exercise 3: Bottom Finder
    
    Objective:
    Find the minimum value stored in an integer BST.
    
    Logic:
    Since it's a BST, the inorder traversal returns sorted values. 
    The minimum value will be the first element of the list.
    """
    # TODO: Implement logic
    pass

def exercise_4_search_value(bst: BinarySearchTree, value: Any) -> bool:
    """
    Exercise 4: Data Search
    
    Objective:
    Check if a specific value exists in the BST.
    
    Logic:
    Use the built-in 'search(data)' method of the BinarySearchTree class.
    """
    # TODO: Implement logic
    pass

def exercise_5_sum_all_values(bst: BinarySearchTree) -> int:
    """
    Exercise 5: Accumulator
    
    Objective:
    Calculate the sum of all integer values stored in the tree.
    
    Logic:
    Get all the values through inorder traversal and return their total sum.
    """
    # TODO: Implement logic
    pass

def exercise_6_values_in_range(bst: BinarySearchTree, min_val: int, max_val: int) -> List[int]:
    """
    Exercise 6: Range Filter
    
    Objective:
    Return a list of all values that fall within the range [min_val, max_val].
    
    Logic:
    Traverse the tree (inorder) and filter the resulting list to keep only 
    elements between min_val and max_val inclusive.
    """
    # TODO: Implement logic
    pass
