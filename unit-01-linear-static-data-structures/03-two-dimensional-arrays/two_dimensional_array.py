"""
File: two_dimensional_array.py
Purpose: Implements a two-dimensional array data structure.
Author: GonzaloQu3dena
Date: 2026-01-22
Version: 1.0

Core concepts to explore:
1. How to implement a two-dimensional array data structure.
2. How to access elements in the array.
3. How to iterate over the array.
4. How to use the matrix as a string.
"""

from typing import List, Iterator, TypeVar, Generic

T = TypeVar('T')

class Matrix(Generic[T]): 
  """
  Represents a two-dimensional array data structure (Row x Col).
  """

  def __init__(self, rows: int, cols: int, default_value: T = None):
    if rows <= 0 or cols <= 0:
      raise ValueError("Rows and columns must be greater than zero.")

    self._rows = rows
    self._cols = cols
    self._data: List[List[T]] = [[default_value for _ in range(cols)] for _ in range(rows)]

  def __getitem__(self, index: tuple[int, int]) -> T:
    """
    Allows access using matrix[row, col].
    """
    row, col = index
    return self._data[row][col]

  def __setitem__(self, index: tuple[int, int], value: T) -> None:
    """
    Allows setting using matrix[row, col] = value.
    """
    row, col = index
    self._data[row][col] = value
  
  def __str__(self) -> str:
    """
    Returns a string representation of the matrix.
    """
    return "\n".join(["\t".join([str(item) for item in row]) for row in self._data])

  def __iter__(self) -> Iterator[T]:
    """
    Iterates over the matrix.
    """
    for row in self._data:
      for item in row:
        yield item

if __name__ == "__main__":
  # 1. Create a matrix of integers.
  matrix = Matrix[int](2, 2, 0)

  # 2. Set the elements of the matrix.
  matrix[0, 0] = 1
  matrix[0, 1] = 2

  # 3. Print the matrix.
  print(matrix)
  