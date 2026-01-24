"""
File: queue.py
Purpose: Implementation of a Queue (FIFO) using a Linked List.
Author: GonzaloQu3dena
Date: 2026-01-23
Version: 1.0
"""

from typing import Generic, TypeVar, Optional, Iterator

T = TypeVar('T')

class Node(Generic[T]):
    """Smallest component of the queue."""
    def __init__(self, data: T):
        self.data: T = data
        self.next: Optional['Node[T]'] = None

    def __repr__(self) -> str:
        return f"Node({self.data})"

class Queue(Generic[T]):
    """
    Implementation of a Queue (FIFO) using a Linked List.
    Maintains references to both 'front' and 'rear' nodes.
    """
    def __init__(self):
        self._front: Optional[Node[T]] = None
        self._rear: Optional[Node[T]] = None
        self._size: int = 0

    def enqueue(self, item: T) -> None:
        """
        Adds an item to the rear of the queue.
        Complexity: O(1)
        """
        new_node = Node[T](item)
        if self.is_empty():
            self._front = new_node
            self._rear = new_node
        else:
            self._rear.next = new_node
            self._rear = new_node
        self._size += 1

    def dequeue(self) -> T:
        """
        Removes and returns the item from the front of the queue.
        Complexity: O(1)
        """
        if self.is_empty():
            raise IndexError("Cannot dequeue from an empty queue.")
        
        data = self._front.data
        self._front = self._front.next
        
        if self._front is None:
            self._rear = None
            
        self._size -= 1
        return data

    def front(self) -> T:
        """
        Returns the item at the front of the queue without removing it.
        Complexity: O(1)
        """
        if self.is_empty():
            raise IndexError("Cannot peek at an empty queue.")
        return self._front.data

    def is_empty(self) -> bool:
        """Returns True if the queue has no items, False otherwise."""
        return self._front is None

    def size(self) -> int:
        """Returns the number of items in the queue."""
        return self._size

    def __iter__(self) -> Iterator[T]:
        """Allows traversal from front to rear."""
        current = self._front
        while current:
            yield current.data
            current = current.next

    def __str__(self) -> str:
        """Returns a visual representation of the queue."""
        if self.is_empty():
            return "Queue is empty"
        
        output = "FRONT -> "
        elements = [str(item) for item in self]
        output += " | ".join(elements)
        output += " <- REAR"
        return output

if __name__ == "__main__":
    # 1. Instantiate the queue
    queue: Queue[str] = Queue[str]()

    # 2. Enqueue elements
    print("Enqueuing elements...")
    queue.enqueue("Patient A")
    queue.enqueue("Patient B")
    queue.enqueue("Patient C")
    print(queue)

    # 3. Front and Dequeue
    print(f"\nFront element: {queue.front()}")
    print(f"Served (Dequeue): {queue.dequeue()}")
    
    print("\nQueue after service:")
    print(queue)
    print(f"Current size: {queue.size()}")
