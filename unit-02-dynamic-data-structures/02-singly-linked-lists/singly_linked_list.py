"""
File: singly_linked_list.py
Purpose: Implementation of a Singly Linked List dynamic data structure.
Author: GonzaloQu3dena
Date: 2026-01-23
Version: 1.0

Core concepts to explore:
1. Node anatomy: Data and Next pointer.
2. Dynamic memory allocation: Fragmented memory usage.
3. Pointer manipulation: Inserting and deleting at the beginning (O(1)).
4. Linear traversal: Accessing elements by index (O(n)).
"""

from typing import Generic, TypeVar, Optional, List

T = TypeVar('T')

class Node(Generic[T]):
    """
    Smallest component of a Linked List.
    Acts like a train car that only knows who is behind it.
    """
    def __init__(self, data: T):
        self.data: T = data
        self.next: Optional['Node[T]'] = None

    def __repr__(self) -> str:
        return f"Node({self.data})"

class SinglyLinkedList(Generic[T]):
    """
    Dynamic data structure consisting of a sequence of nodes.
    Supports efficient insertion and deletion at the beginning.
    """

    def __init__(self):
        self._head: Optional[Node[T]] = None
        self._tail: Optional[Node[T]] = None
        self._size: int = 0

    def push_front(self, data: T) -> None:
        """
        Inserts a new node at the start of the list.
        Complexity: O(1)
        """
        new_node = Node[T](data)
        if not self._head:
            self._head = new_node
            self._tail = new_node
        else:
            new_node.next = self._head
            self._head = new_node
        self._size += 1

    def push_back(self, data: T) -> None:
        """
        Inserts a new node at the end of the list.
        Complexity: O(1) thanks to the tail pointer.
        """
        new_node = Node[T](data)
        if not self._head:
            self._head = new_node
            self._tail = new_node
        else:
            self._tail.next = new_node
            self._tail = new_node
        self._size += 1

    def pop_front(self) -> T:
        """
        Removes and returns the data from the first node.
        Complexity: O(1)
        """
        if not self._head:
            raise IndexError("Cannot remove from an empty list.")
        
        data = self._head.data
        self._head = self._head.next
        
        if not self._head:
            self._tail = None
            
        self._size -= 1
        return data

    def get(self, index: int) -> T:
        """
        Retrieves the data at the specified index.
        Complexity: O(n) - Must traverse from the head.
        """
        if index < 0 or index >= self._size:
            raise IndexError("Index out of bounds.")
        
        current = self._head
        for _ in range(index):
            current = current.next
        return current.data

    def size(self) -> int:
        """Returns the current number of nodes in the list."""
        return self._size

    def __str__(self) -> str:
        """Returns a string representation of the list."""
        nodes: List[str] = []
        current = self._head
        while current:
            nodes.append(str(current.data))
            current = current.next
        return " -> ".join(nodes) + " -> None"

if __name__ == "__main__":
    # 1. Instantiate the list (explicitly string-based)
    linked_list: SinglyLinkedList[str] = SinglyLinkedList()

    # 2. Add elements
    print("Adding elements...")
    linked_list.push_front("Second")
    linked_list.push_front("First")
    linked_list.push_back("Third")
    linked_list.push_back("Fourth")

    print(f"Current List: {linked_list}")
    print(f"Size: {linked_list.size()}")

    # 3. Access elements
    print(f"Element at index 0: {linked_list.get(0)}")
    print(f"Element at index 2: {linked_list.get(2)}")

    # 4. Remove elements
    print(f"Removed from beginning: {linked_list.pop_front()}")
    print(f"Removed from beginning: {linked_list.pop_front()}")

    print(f"Final List: {linked_list}")
    print(f"Final Size: {linked_list.size()}")
