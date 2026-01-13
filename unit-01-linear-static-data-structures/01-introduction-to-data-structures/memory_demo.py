"""
File: memory_demo.py
Purpose: Demonstrates that variables in Python function as labels (references) 
         pointing to objects stored in the Heap memory.
Author: GonzaloQu3dena
Date: 2026-01-13
Version: 1.0

Core concepts to explore:
1. Difference between mutable (lists, dicts) and immutable (ints, strings) objects.
2. How the Stack (references) and the Heap (objects) interact in the Python runtime.
3. Impact of shared references on data integrity.
"""

def demo_mutability():
  """
  Demonstrates mutability and the behavior of shared references in Python.

  This function creates a list in the Heap and two references in the Stack 
  pointing to the same memory address. It shows how modifying the object 
  through one reference affects all other references pointing to it.
  """

  print("\n--- Mutability and Shared References ---")
  # Create a list (Object in the Heap)
  list_a = [1, 2, 3]
  # Create a reference to the same object in the Heap
  list_b = list_a

  print(f"Original list_a: {list_a}")

  # Modify using the reference 
  list_b.append(4)

  # Print the result of the modification
  print(f"A after modifying with B: {list_a}")
  print(f"Are the same object? {list_a is list_b}")
  print(f"Memory ID of list_a: {hex(id(list_a))}")
  print(f"Memory ID of list_b: {hex(id(list_b))}")

if __name__ == "__main__":
  demo_mutability()