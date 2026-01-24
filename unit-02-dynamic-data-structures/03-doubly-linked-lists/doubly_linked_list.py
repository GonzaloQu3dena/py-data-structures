from typing import Generic, TypeVar, Optional, List, Iterator

T = TypeVar('T')

class Node(Generic[T]):
    """
    Smallest component of a Linked List.
    Acts like a train car that knows both who is behind it and who is in front of it.
    """
    def __init__(self, data: T):
        self.data: T = data
        self.next: Optional['Node[T]'] = None
        self.prev: Optional['Node[T]'] = None

class DoublyLinkedList(Generic[T]):
    """
    Dynamic data structure consisting of a sequence of nodes.
    Supports efficient insertion and deletion at the beginning and end.
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
            self._head.prev = new_node
            self._head = new_node
        self._size += 1

    def push_back(self, data: T) -> None:
        """
        Inserts a new node at the end of the list.
        Complexity: O(1)
        """
        new_node = Node[T](data)
        if not self._head:
            self._head = new_node
            self._tail = new_node
        else:
            self._tail.next = new_node
            new_node.prev = self._tail
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
        else:
            self._head.prev = None
        self._size -= 1
        return data

    def pop_back(self) -> T:
        """
        Removes and returns the data from the last node.
        Complexity: O(1)
        """
        if not self._tail:
            raise IndexError("Cannot remove from an empty list.")
        
        data = self._tail.data
        self._tail = self._tail.prev
        
        if not self._tail:
            self._head = None
        else:
            self._tail.next = None
            
        self._size -= 1
        return data

    def get(self, index: int) -> T:
        """
        Retrieves the data at the specified index.
        Complexity: O(n) - Can traverse from head or tail depending on index.
        """
        if index < 0 or index >= self._size:
            raise IndexError("Index out of bounds.")
        
        if index < self._size // 2:
            current = self._head
            for _ in range(index):
                current = current.next
        else:
            current = self._tail
            for _ in range(self._size - 1, index, -1):
                current = current.prev
        
        return current.data
    
    def size(self) -> int:
        """Returns the current number of nodes in the list."""
        return self._size

    def __str__(self) -> str:
        """Returns a string representation of the list."""
        nodes: List[str] = []
        for element in self:
            nodes.append(str(element))
        return " <-> ".join(nodes)

    def is_empty(self) -> bool:
        """Returns True if the list is empty, False otherwise."""
        return self._size == 0

    def __iter__(self) -> Iterator[T]:
        """Returns a forward iterator over the list."""
        current = self._head
        while current:
            yield current.data
            current = current.next

    def backward_iter(self) -> Iterator[T]:
        """Returns a backward iterator over the list."""
        current = self._tail
        while current:
            yield current.data
            current = current.prev

if __name__ == "__main__":
    # 1. Instantiate the list
    linked_list: DoublyLinkedList[str] = DoublyLinkedList[str]()

    # 2. Add elements
    print("Adding elements...")
    linked_list.push_front("Second")
    linked_list.push_front("First")
    linked_list.push_back("Third")
    linked_list.push_back("Fourth")
    
    print(f"Current List: {linked_list}")
    print(f"Size: {linked_list.size()}")

    # 3. Access elements (forward traversal)
    print("Forward traversal:")
    for element in linked_list:
        print(f"Element: {element}")

    # 4. Access elements (backward traversal)
    print("Backward traversal:")
    for element in linked_list.backward_iter():
        print(f"Element: {element}")

    # 5. Remove elements
    print(f"Removed from beginning: {linked_list.pop_front()}")
    print(f"Removed from beginning: {linked_list.pop_front()}")
    
    print(f"Final List: {linked_list}")
    print(f"Final Size: {linked_list.size()}")