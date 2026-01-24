from typing import Generic, TypeVar, Optional, List, Iterator

T = TypeVar('T')

class Node(Generic[T]):
    """
    Smallest component of a Linked List.
    In a circular list, the last node points back to the first.
    """
    def __init__(self, data: T):
        self.data: T = data
        self.next: Optional['Node[T]'] = None

    def __repr__(self) -> str:
        return f"Node({self.data})"

class CircularLinkedList(Generic[T]):
    """
    Dynamic data structure where the last node points to the first.
    This implementation uses a 'tail' pointer for O(1) access to both ends.
    """
    def __init__(self):
        self._tail: Optional[Node[T]] = None
        self._size: int = 0

    def push_front(self, data: T) -> None:
        """
        Inserts a new node at the start of the list.
        Complexity: O(1)
        """
        new_node = Node[T](data)
        if not self._tail:
            new_node.next = new_node
            self._tail = new_node
        else:
            new_node.next = self._tail.next
            self._tail.next = new_node
        self._size += 1

    def push_back(self, data: T) -> None:
        """
        Inserts a new node at the end of the list.
        Complexity: O(1)
        """
        self.push_front(data)
        self._tail = self._tail.next

    def pop_front(self) -> T:
        """
        Removes and returns the data from the first node.
        Complexity: O(1)
        """
        if not self._tail:
            raise IndexError("Cannot remove from an empty list.")
        
        head = self._tail.next
        data = head.data
        
        if self._size == 1:
            self._tail = None
        else:
            self._tail.next = head.next
            
        self._size -= 1
        return data

    def get(self, index: int) -> T:
        """
        Retrieves the data at the specified index.
        Complexity: O(n)
        """
        if index < 0 or index >= self._size:
            raise IndexError("Index out of bounds.")
        
        current = self._tail.next  # Start at head
        for _ in range(index):
            current = current.next
        return current.data

    def size(self) -> int:
        """Returns the current number of nodes in the list."""
        return self._size

    def is_empty(self) -> bool:
        """Returns True if the list is empty, False otherwise."""
        return self._size == 0

    def __iter__(self) -> Iterator[T]:
        """Returns an iterator over the list."""
        if not self._tail:
            return
        
        head = self._tail.next
        current = head
        for _ in range(self._size):
            yield current.data
            current = current.next

    def __str__(self) -> str:
        """Returns a string representation of the list."""
        if not self._tail:
            return "Empty Circular List"
        
        nodes: List[str] = []
        for element in self:
            nodes.append(f"[{element}]")
        
        return " -> ".join(nodes) + " -> (back to head)"

if __name__ == "__main__":
    # 1. Instantiate the list
    linked_list: CircularLinkedList[str] = CircularLinkedList[str]()

    # 2. Add elements
    print("Adding elements...")
    linked_list.push_back("First")
    linked_list.push_back("Second")
    linked_list.push_back("Third")
    linked_list.push_front("Zero")

    print(f"Current List: {linked_list}")
    print(f"Size: {linked_list.size()}")

    # 3. Access elements
    print("Traversal:")
    for element in linked_list:
        print(f"Element: {element}")

    # 4. Remove elements
    print(f"Removed from beginning: {linked_list.pop_front()}")
    print(f"Removed from beginning: {linked_list.pop_front()}")

    print(f"Final List: {linked_list}")
    print(f"Final Size: {linked_list.size()}")
