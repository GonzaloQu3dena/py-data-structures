"""
File: general_tree.py
Purpose: Implementation of a General Tree where each node can have N children.
Author: GonzaloQu3dena
Date: 2026-01-26
Version: 1.0
"""

from collections import deque
from typing import Generic, TypeVar, Optional, List, Deque

T = TypeVar('T')

class Node(Generic[T]):
    """
    A passive node in a General Tree.
    Contains only data and references to children (no methods).
    """
    def __init__(self, data: T):
        self.data: T = data
        self.children: List['Node[T]'] = []

    def __repr__(self) -> str:
        return f"Node({self.data})"

class GeneralTree(Generic[T]):
    """
    Implementation of a General Tree data structure.
    All tree operations are handled through the tree class methods.
    """
    def __init__(self, root_data: Optional[T] = None):
        self._root: Optional[Node[T]] = Node[T](root_data) if root_data is not None else None

    def is_empty(self) -> bool:
        """Returns True if the tree has no root."""
        return self._root is None

    def add_child(self, parent_data: T, child_data: T) -> bool:
        """
        Adds a child node to the parent node with the specified data.
        Returns True if successful, False if parent not found.
        """
        if self.is_empty():
            return False
        
        parent_node = self._find_node(self._root, parent_data)

        if parent_node:
            parent_node.children.append(Node[T](child_data))
            return True

        return False

    def get_height(self) -> int:
        """
        Calculates the height of the tree (longest path from root to leaf).
        Complexity: O(n)
        """
        if self.is_empty():
            return 0
        return self._get_height_recursive(self._root)

    def preorder(self) -> List[T]:
        """
        Depth-First Search: Preorder Traversal (Node -> Children).
        Complexity: O(n)
        """
        if self.is_empty():
            return []
        return self._preorder_recursive(self._root)

    def postorder(self) -> List[T]:
        """
        Depth-First Search: Postorder Traversal (Children -> Node).
        Complexity: O(n)
        """
        if self.is_empty():
            return []
        return self._postorder_recursive(self._root)

    def inorder(self) -> List[T]:
        """
        Depth-First Search: Inorder Traversal (Left -> Node -> Right).
        Complexity: O(n)
        """
        if self.is_empty():
            return []
        return self._inorder_recursive(self._root)

    def level_order(self) -> List[T]:
        """
        Breadth-First Search: Level Order Traversal.
        Complexity: O(n)
        """
        if self.is_empty():
            return []
        
        result = []
        queue: Deque[Node[T]] = deque[Node[T] | None]([self._root])
        
        while queue:
            current = queue.popleft()
            result.append(current.data)
            for child in current.children:
                queue.append(child)
                
        return result

    def is_leaf(self, node_data: T) -> bool:
        """Returns True if the node has no children."""
        node = self._find_node(self._root, node_data)
        return len(node.children) == 0 if node else False

    def _find_node(self, node: Optional[Node[T]], target_data: T) -> Optional[Node[T]]:
        """Recursively searches for a node with the given data."""
        if node is None:
            return None
        
        if node.data == target_data:
            return node
        
        for child in node.children:
            result = self._find_node(child, target_data)
            if result:
                return result
        
        return None

    def _get_height_recursive(self, node: Optional[Node[T]]) -> int:
        """Recursively calculates the height of the tree."""
        if node is None or len(node.children) == 0:
            return 0
        
        max_child_height = 0

        for child in node.children:
            max_child_height = max(max_child_height, self._get_height_recursive(child))
        
        return 1 + max_child_height

    def _preorder_recursive(self, node: Optional[Node[T]]) -> List[T]:
        """Recursively traverses the tree in preorder."""
        if node is None:
            return []
        
        result = [node.data]

        for child in node.children:
            result.extend(self._preorder_recursive(child))
            
        return result

    def _postorder_recursive(self, node: Optional[Node[T]]) -> List[T]:
        """Recursively traverses the tree in postorder."""
        if node is None:
            return []
        
        result = []

        for child in node.children:
            result.extend(self._postorder_recursive(child))
        result.append(node.data)
            
        return result

    def _inorder_recursive(self, node: Optional[Node[T]]) -> List[T]:
        """Recursively traverses the tree in inorder."""
        if node is None:
            return []
        
        result = []

        for child in node.children:
            result.extend(self._inorder_recursive(child))
        result.append(node.data)

        return result

    def _render_tree(self, node: Node[T], level: int = 0) -> str:
        """Recursively renders the tree structure with indentation."""
        indent = "  " * level
        res = f"{indent}└── {node.data}\n"
        for child in node.children:
            res += self._render_tree(child, level + 1)
        return res

    def __str__(self) -> str:
        """Returns a string representation of the tree (indented)."""
        if self.is_empty():
            return "Empty Tree"
        return self._render_tree(self._root).strip()

if __name__ == "__main__":
    
    # 1. Build the tree
    tree = GeneralTree[str]("CEO")
    
    # 2. Add children to the tree
    tree.add_child("CEO", "VP Operations")
    tree.add_child("CEO", "VP Technology")
    tree.add_child("VP Operations", "Manager A")
    tree.add_child("VP Technology", "Manager B")
    tree.add_child("VP Technology", "Manager C")
    
    # 3. Print the tree
    print(tree)
    
    # 4. Print the tree height
    print(f"\nTree Height: {tree.get_height()}")
    
    # 5. Print the tree traversal
    print(f"Preorder: {tree.preorder()}")
    print(f"Inorder: {tree.inorder()}")
    print(f"Postorder: {tree.postorder()}")

    # 6. Print the tree level order
    print(f"Level Order (BFS): {tree.level_order()}")
