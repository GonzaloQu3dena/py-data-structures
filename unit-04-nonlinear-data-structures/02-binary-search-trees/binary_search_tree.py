"""
File: binary_search_tree.py
Purpose: Implementation of a Binary Search Tree (BST) with automatic ordering.
Author: GonzaloQu3dena
Date: 2026-02-05
Version: 1.0
"""

from typing import Generic, TypeVar, Optional, List, Callable

T = TypeVar('T')

class Node(Generic[T]):
    """
    A passive node in a Binary Search Tree.
    Contains data and references to left and right children.
    """
    def __init__(self, data: T):
        self.data: T = data
        self.left: Optional['Node[T]'] = None
        self.right: Optional['Node[T]'] = None

    def __repr__(self) -> str:
        return f"Node({self.data})"

class BinarySearchTree(Generic[T]):
    """
    Implementation of a Binary Search Tree data structure.
    BST Property: Left < Node < Right.
    
    Args:
        comp: Optional lambda function that compares two elements (a, b).
              Should return True if a < b, False otherwise.
              Example: lambda p1, p2: p1.id < p2.id
    """
    def __init__(self, comp: Optional[Callable[[T, T], bool]] = None):
        self._root: Optional[Node[T]] = None
        # Default to standard less-than comparison
        self._comp: Callable[[T, T], bool] = comp if comp is not None else lambda a, b: a < b

    def is_empty(self) -> bool:
        """Returns True if the tree has no root."""
        return self._root is None

    def insert(self, data: T) -> None:
        """
        Inserts a new value into the BST following the ordering rules.
        Complexity: Average O(log n), Worst O(n)
        """
        if self.is_empty():
            self._root = Node[T](data)
        else:
            self._insert_recursive(self._root, data)

    def search(self, data: T) -> bool:
        """
        Searches for a value in the BST.
        Complexity: Average O(log n), Worst O(n)
        """
        return self._search_recursive(self._root, data) is not None

    def delete(self, data: T) -> bool:
        """
        Removes a value from the BST while maintaining its property.
        Returns True if the value was found and deleted.
        Complexity: Average O(log n), Worst O(n)
        """
        if self.search(data):
            self._root = self._delete_recursive(self._root, data)
            return True
        return False

    def inorder(self) -> List[T]:
        """
        Inorder Traversal (L-N-R). In a BST, this returns sorted values.
        Complexity: O(n)
        """
        return self._inorder_recursive(self._root)

    def _insert_recursive(self, node: Node[T], data: T) -> None:
        """Recursively finds the correct position for the new data."""
        if self._comp(data, node.data):
            if node.left is None:
                node.left = Node[T](data)
            else:
                self._insert_recursive(node.left, data)
        elif self._comp(node.data, data):
            if node.right is None:
                node.right = Node[T](data)
            else:
                self._insert_recursive(node.right, data)

    def _search_recursive(self, node: Optional[Node[T]], data: T) -> Optional[Node[T]]:
        """Recursively searches for data using the comparison function."""
        if node is None:
            return None
        
        # Check equality: not (a < b) and not (b < a)
        if not self._comp(data, node.data) and not self._comp(node.data, data):
            return node
        
        if self._comp(data, node.data):
            return self._search_recursive(node.left, data)
        
        return self._search_recursive(node.right, data)

    def _delete_recursive(self, node: Optional[Node[T]], data: T) -> Optional[Node[T]]:
        """Recursively deletes a node and restructures the tree."""
        if node is None:
            return None

        if self._comp(data, node.data):
            node.left = self._delete_recursive(node.left, data)
        elif self._comp(node.data, data):
            node.right = self._delete_recursive(node.right, data)
        else:
            # Node found. Handle the 3 cases:
            
            # Case 1 & 2: No child or only one child
            if node.left is None:
                return node.right
            elif node.right is None:
                return node.left

            # Case 3: Two children
            # Find the in-order successor (smallest in the right subtree)
            successor = self._min_value_node(node.right)
            node.data = successor.data
            # Delete the successor
            node.right = self._delete_recursive(node.right, successor.data)

        return node

    def _min_value_node(self, node: Node[T]) -> Node[T]:
        """Finds the node with the minimum value in a subtree."""
        current = node
        while current.left is not None:
            current = current.left
        return current

    def _inorder_recursive(self, node: Optional[Node[T]]) -> List[T]:
        """Recursively performs inorder traversal."""
        if node is None:
            return []
        return self._inorder_recursive(node.left) + [node.data] + self._inorder_recursive(node.right)

if __name__ == "__main__":
    
    # 1. Build the BST with integers
    bst_int = BinarySearchTree[int]()
    values = [50, 30, 70, 20, 40, 60, 80]
    
    # 2. Insert values into the BST
    for v in values:
        bst_int.insert(v)
    
    # 3. Print the inorder traversal (sorted)
    print(f"\nInorder (Sorted): {bst_int.inorder()}")
    
    # 4. Search for values
    print(f"Search 40: {'Found' if bst_int.search(40) else 'Not Found'}")
    print(f"Search 90: {'Found' if bst_int.search(90) else 'Not Found'}")
    
    # 5. Delete values
    bst_int.delete(20)
    bst_int.delete(30)
    bst_int.delete(50)
    
    # 6. Print the inorder traversal after deletions
    print(f"\nInorder after deletions: {bst_int.inorder()}\n")
    
    # 7. Define a simple entity class
    class Person:
        def __init__(self, id: int, name: str):
            self.id = id
            self.name = name
        
        def __repr__(self) -> str:
            return f"Person(id={self.id}, name='{self.name}')"
    
    # 8. Create BST with custom comparison lambda (comparing two objects)
    bst_person = BinarySearchTree[Person](comp=lambda p1, p2: p1.id < p2.id)
    
    # 9. Insert people into the BST
    people = [
        Person(50, "Alice"),
        Person(30, "Bob"),
        Person(70, "Charlie"),
        Person(20, "Diana"),
        Person(40, "Eve"),
    ]
    
    # 10. Print the people inserted into the BST
    for person in people:
        bst_person.insert(person)
    
    # 11. Print the inorder traversal (sorted by id)
    for person in bst_person.inorder():
        print(f"  - {person}")
    
    print(f"\nSearch Person(id=40): {'Found' if bst_person.search(Person(40, '')) else 'Not Found'}")
    print(f"Search Person(id=99): {'Found' if bst_person.search(Person(99, '')) else 'Not Found'}")
