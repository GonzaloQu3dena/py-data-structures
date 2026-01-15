"""
File: static_array.py
Purpose: Implements a static array data structure with a fixed capacity.
Author: GonzaloQu3dena
Date: 2026-01-14
Version: 1.0

Core concepts to explore:
1. How to implement a static array data structure with a fixed capacity.
2. How to add, insert, delete and get elements from the array.
3. How to check if the array is full or empty.
"""

from typing import Any, Optional

class StaticArray:  
  """
  Represents a static array data structure with a fixed capacity.

  Attributes:
    _capacity: The maximum number of elements the array can hold.
    _length: The current number of elements in the array.
    _data: The list of elements in the array.

  Methods:
    _is_full: Checks if the array is full.
    is_empty: Checks if the array is empty.
    push_back: Adds an element to the end of the array.
    pop_back: Removes the last element from the array.
    insert: Inserts an element at a given index.
    delete: Removes an element at a given index.
    get: Returns the element at a given index.
  """

  def __init__(self, capacity: int):
    """
    Initializes the static array with a given capacity.

    Args:
      capacity: The maximum number of elements the array can hold.
    """
    self._capacity = capacity
    self._length = 0
    self._data: list[Optional[Any]] = [None] * capacity

  def _is_full(self) -> bool:
    """
    Checks if the array is full.

    Returns:
      bool: True if the array is full, False otherwise.
    """
    return self._length == self._capacity

  def is_empty(self) -> bool:
    """
    Checks if the array is empty.

    Returns:
      bool: True if the array is empty, False otherwise.
    """
    return self._length == 0

  def push_back(self, value: Any) -> None:
    """
    Adds an element to the end of the array.

    Args:
      value: The element to add to the array.
    """
    if self._is_full():
      raise ValueError("Array is full")
    
    self._data[self._length] = value
    self._length += 1

  def pop_back(self) -> Any:
    """
    Removes the last element from the array.

    Returns:
      Any: The last element of the array.
    """
    if self.is_empty():
      raise ValueError("Array is empty")
    self._length -= 1
    return self._data[self._length]

  def insert(self, index: int, value: Any) -> None:
    """
    Inserts an element at a given index.

    Args:
      index: The index at which to insert the element.
      value: The element to insert.
    """
    if self._is_full():
      raise ValueError("Array is full")

    if index < 0 or index > self._length:
      raise ValueError("Index out of bounds")

    for i in range(self._length, index, -1):
      self._data[i] = self._data[i - 1]

    self._data[index] = value
    self._length += 1

  def delete(self, index:int) -> None:
    """
    Removes an element at a given index.

    Args:
      index: The index of the element to remove.
    """
    if self.is_empty():
      raise ValueError("Array is empty")

    if index < 0 or index >= self._length:
      raise ValueError("Index out of bounds")

    for i in range(index, self._length - 1):
      self._data[i] = self._data[i + 1]

    self._data[self._length - 1] = None
    self._length -= 1

  def get(self, index:int) -> Any:
    """
    Returns the element at a given index.

    Args:
      index: The index of the element to return.

    Returns:
      Any: The element at the given index.
    """
    if index < 0 or index >= self._length:
      raise ValueError("Index out of bounds")
    return self._data[index]

  def set(self, index:int, value:Any) -> None:
    """
    Sets the element at a given index.

    Args:
      index: The index of the element to set.
      value: The element to set.
    """
    if index < 0 or index >= self._length:
      raise ValueError("Index out of bounds")
    self._data[index] = value

  
if __name__ == "__main__":
  # 1. Create a static array with capacity for 5 elements
  mi_arreglo = StaticArray(5)
  print(f"Capacity: {mi_arreglo._capacity}, Length: {mi_arreglo._length}")

  # 2. Add elements to the end (Push)
  mi_arreglo.push_back(10)
  mi_arreglo.push_back(20)
  mi_arreglo.push_back(30)
  print(f"Current state: {[mi_arreglo.get(i) for i in range(mi_arreglo._length)]}")

  # 3. Insert an element at a specific index (index 1)
  mi_arreglo.insert(1, 15)
  print(f"After inserting: {[mi_arreglo.get(i) for i in range(mi_arreglo._length)]}")

  # 4. Delete an element (index 2)
  mi_arreglo.delete(2)
  print(f"After deleting: {[mi_arreglo.get(i) for i in range(mi_arreglo._length)]}")

  # 5. Remove the last element (Pop)
  ultimo = mi_arreglo.pop_back()
  print(f"Extracted element: {ultimo}")
  print(f"Final array: {[mi_arreglo.get(i) for i in range(mi_arreglo._length)]}")
  print(f"Final length: {mi_arreglo._length}")