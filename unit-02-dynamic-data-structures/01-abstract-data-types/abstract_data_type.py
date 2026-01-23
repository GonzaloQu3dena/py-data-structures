"""
File: abstract_data_type.py
Purpose: Illustrates the concept of Abstract Data Types (ADT) using ABCs.
Author: GonzaloQu3dena
Date: 2026-01-22
Version: 1.0

Core concepts to explore:
1. Difference between Interface (ADT) and Implementation.
2. Using Abstract Base Classes (ABC) to define a contract.
3. Encapsulation of internal state.
"""

from abc import ABC, abstractmethod
from typing import Any, List

class DataContainer(ABC):
    """
    Abstract Data Type (ADT) representing a generic data container.
    Only defines WHAT operations are possible, not HOW.
    """

    @abstractmethod
    def add(self, item: Any) -> None:
        """Adds an item to the container."""
        pass

    @abstractmethod
    def remove(self) -> Any:
        """Removes and returns an item from the container."""
        pass

    @abstractmethod
    def size(self) -> int:
        """Returns the number of items in the container."""
        pass

class StackImplementation(DataContainer):
    """
    Concrete implementation of the DataContainer ADT using a List.
    Follows a Last-In, First-Out (LIFO) logic.
    """

    def __init__(self):
        # Encapsulation: the internal list is private
        self._items: List[Any] = []

    def add(self, item: Any) -> None:
        """Adds an item to the top of the stack."""
        self._items.append(item)

    def remove(self) -> Any:
        """Removes the last item added."""
        if self.size() == 0:
            raise IndexError("Cannot remove from an empty stack.")
        return self._items.pop()

    def size(self) -> int:
        """Returns the current size of the stack."""
        return len(self._items)

    def __str__(self) -> str:
        return f"Stack: {self._items}"

if __name__ == "__main__":
    # 1. Instantiate the concrete implementation
    # Note: We treat it as its abstract type (the ADT)
    my_container: DataContainer = StackImplementation()

    # 2. Use the defined operations
    my_container.add("Python")
    my_container.add("Data Structures")
    my_container.add(2026)

    print(f"Container state: {my_container}")
    print(f"Size: {my_container.size()}")

    # 3. Remove an item
    removed = my_container.remove()
    print(f"Removed item: {removed}")
    print(f"Final state: {my_container}")
