"""
File: priority_queue.py
Purpose: Implementation of a Priority Queue using a Sorted Linked List.
Author: GonzaloQu3dena
Date: 2026-01-23
Version: 1.0
"""

from typing import Generic, TypeVar, Optional, Iterator

T = TypeVar('T')

class Node(Generic[T]):
    """Component of the priority queue that stores data and its priority."""
    def __init__(self, data: T, priority: int):
        self.data: T = data
        self.priority: int = priority
        self.next: Optional['Node[T]'] = None

    def __repr__(self) -> str:
        return f"Node({self.data}, priority={self.priority})"

class PriorityQueue(Generic[T]):
    """
    Implementation of a Max-Priority Queue using a Sorted Linked List.
    Higher priority values are served first.
    """
    def __init__(self):
        self._front: Optional[Node[T]] = None
        self._size: int = 0

    def enqueue(self, item: T, priority: int) -> None:
        """
        Inserts an item into the queue based on its priority.
        Complexity: O(n)
        """
        new_node = Node[T](item, priority)

        # Case 1: Empty list or new node has higher priority than the head
        if self.is_empty() or priority > self._front.priority:
            new_node.next = self._front
            self._front = new_node
        else:
            # Case 2: Traverse to find the correct insertion spot
            current = self._front
            while current.next and current.next.priority >= priority:
                current = current.next
            
            new_node.next = current.next
            current.next = new_node
            
        self._size += 1

    def dequeue(self) -> T:
        """
        Removes and returns the item with the highest priority.
        Complexity: O(1)
        """
        if self.is_empty():
            raise IndexError("Cannot dequeue from an empty priority queue.")
        
        data = self._front.data
        self._front = self._front.next
        self._size -= 1
        return data

    def peek(self) -> T:
        """
        Returns the highest priority item without removing it.
        Complexity: O(1)
        """
        if self.is_empty():
            raise IndexError("Cannot peek at an empty priority queue.")
        return self._front.data

    def is_empty(self) -> bool:
        """Returns True if the queue has no items, False otherwise."""
        return self._front is None

    def size(self) -> int:
        """Returns the number of items in the queue."""
        return self._size

    def __iter__(self) -> Iterator[T]:
        """Allows traversal from highest to lowest priority."""
        current = self._front
        while current:
            yield current.data
            current = current.next

    def __str__(self) -> str:
        """Returns a standard visual representation of the priority queue."""
        if self.is_empty():
            return "Priority Queue is empty"
        
        nodes = []
        current = self._front
        while current:
            nodes.append(f"[{current.data} | P:{current.priority}]")
            current = current.next
        
        return "FRONT -> " + " -> ".join(nodes) + " -> REAR"

if __name__ == "__main__":
    # 1. Instantiate the priority queue
    pq: PriorityQueue[str] = PriorityQueue[str]()

    # 2. Enqueue elements with different priorities
    print("Enqueuing patients at ER...")
    pq.enqueue("Flu", 2)
    pq.enqueue("Heart Attack", 10)
    pq.enqueue("Broken Arm", 5)
    pq.enqueue("Fever", 2)

    print(pq)

    # 3. Serve the highest priority patient
    print(f"\nServing most urgent: {pq.dequeue()}")
    print(f"Next in line: {pq.peek()}")
    
    print("\nQueue after service:")
    print(pq)
    print(f"Current size: {pq.size()}")
