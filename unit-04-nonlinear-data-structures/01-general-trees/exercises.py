"""
File: exercises.py
Purpose: LAB: GENERAL TREE CHALLENGES
Author: GonzaloQu3dena
Date: 2026-01-26
Version: 1.1
"""

from typing import Any, List, Optional
from general_tree import GeneralTree

def exercise_1_count_all_nodes(tree: GeneralTree) -> int:
    """
    Exercise 1: Count All Nodes
    
    Objective:
    Count the total number of nodes in the tree.
    
    Logic:
    Use a traversal method (e.g. preorder) to get all the data and return the number of elements in the result list.
    """
    # TODO: Implement logic
    pass

def exercise_2_find_max_value(tree: GeneralTree) -> Optional[int]:
    """
    Exercise 2: Peak Value
    
    Objective:
    Find the maximum value stored in an integer tree.
    
    Logic:
    Get all the data from the tree and use an aggregation function to find the highest value.
    """
    # TODO: Implement logic
    pass

def exercise_3_count_leaves(tree: GeneralTree) -> int:
    """
    Exercise 3: Leaf Counter
    
    Objective:
    Count the number of leaf nodes (nodes with no children) in the tree.
    
    Logic:
    Traverse all the elements of the tree and, for each one, 
    check if it is a leaf using the 'tree.is_leaf(data)' method.
    """
    # TODO: Implement logic
    pass

def exercise_4_get_all_leaves_values(tree: GeneralTree) -> List[Any]:
    """
    Exercise 4: Harvesting Leaves
    
    Objective:
    Return a list with the values ('data') of all the leaf nodes.
    
    Logic:
    Filter the complete list of tree nodes keeping only those where 'tree.is_leaf(data)' is True.
    """
    # TODO: Implement logic
    pass

def exercise_5_file_system_size(tree: GeneralTree) -> int:
    """
    Exercise 5: Disk Usage
    
    Objective:
    Calculate the total size of the tree by summing all the values of 'data'.
    (Simulate a file system where each node has a size).
    
    Logic:
    Get all the values through a traversal and return their total sum.
    """
    # TODO: Implement logic
    pass

def exercise_6_dom_search_by_tag(tree: GeneralTree, tag_name: str) -> List[Any]:
    """
    Exercise 6: HTML DOM Search
    
    Objective:
    Simulate a search in the DOM returning all the values that match 
    exactly with 'tag_name'.
    
    Logic:
    Traverse the tree and filter the elements that are exactly equal to the searched tag.
    """
    # TODO: Implement logic
    pass