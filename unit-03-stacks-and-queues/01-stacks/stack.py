"""
File: stack.py
Purpose: Implementation of a Stack (LIFO) using a Linked List.
Author: GonzaloQu3dena
Date: 2026-01-23
Version: 1.0
"""

from typing import Generic, TypeVar, Optional, Iterator

T = TypeVar('T')

class Node(Generic[T]):
    """Smallest component of the stack."""
    def __init__(self, data: T):
        self.data: T = data
        self.next: Optional['Node[T]'] = None

    def __repr__(self) -> str:
        return f"Node({self.data})"

class Stack(Generic[T]):
    """
    Implementation of a Stack (LIFO) using a Linked List.
    Maintains a reference to the 'top' node.
    """
    def __init__(self):
        self._top: Optional[Node[T]] = None
        self._size: int = 0

    def push(self, item: T) -> None:
        """
        Adds an item to the top of the stack.
        Complexity: O(1)
        """
        new_node = Node[T](item)
        new_node.next = self._top
        self._top = new_node
        self._size += 1

    def pop(self) -> T:
        """
        Removes and returns the item from the top of the stack.
        Complexity: O(1)
        """
        if self.is_empty():
            raise IndexError("Cannot pop from an empty stack.")
        
        data = self._top.data
        self._top = self._top.next
        self._size -= 1
        return data

    def peek(self) -> T:
        """
        Returns the item at the top of the stack without removing it.
        Complexity: O(1)
        """
        if self.is_empty():
            raise IndexError("Cannot peek at an empty stack.")
        return self._top.data

    def is_empty(self) -> bool:
        """Returns True if the stack has no items, False otherwise."""
        return self._top is None

    def size(self) -> int:
        """Returns the number of items in the stack."""
        return self._size

    def __iter__(self) -> Iterator[T]:
        """Allows traversal from top to bottom."""
        current = self._top
        while current:
            yield current.data
            current = current.next

    def __str__(self) -> str:
        """Returns a visual representation of the stack with its Top reference."""
        if self.is_empty():
            return "Stack is empty"
        
        output = "\n[STACK VIEW]\n"
        current = self._top
        is_first = True
        
        while current:
            prefix = "TOP -> " if is_first else "       "
            output += f"{prefix}[{current.data}]\n"
            current = current.next
            is_first = False
            
        output += "       ---"
        return output

if __name__ == "__main__":
    # 1. Instantiate the stack
    stack: Stack[int] = Stack[int]()

    # 2. Push elements
    print("Pushing elements...")
    stack.push(10)
    stack.push(20)
    stack.push(30)
    print(stack)

    # 3. Peek and Pop
    print(f"\nPeek element: {stack.peek()}")
    print(f"Pop element: {stack.pop()}")
    
    print("\nStack after pop:")
    print(stack)
    print(f"Current size: {stack.size()}")