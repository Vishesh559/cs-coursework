"""
Binary Search Tree (BST) Implementation
----------------------------------------
Supports: insert, search, delete, in-order/pre-order/post-order traversal,
height calculation, and min/max retrieval.

Time Complexity (average case, balanced tree): O(log n) for insert/search/delete
Time Complexity (worst case, skewed tree): O(n)
Space Complexity: O(n)
"""

from typing import Optional, List


class Node:
    def __init__(self, key: int):
        self.key = key
        self.left: Optional["Node"] = None
        self.right: Optional["Node"] = None


class BinarySearchTree:
    def __init__(self):
        self.root: Optional[Node] = None

    # ---------- Insert ----------
    def insert(self, key: int) -> None:
        self.root = self._insert(self.root, key)

    def _insert(self, node: Optional[Node], key: int) -> Node:
        if node is None:
            return Node(key)
        if key < node.key:
            node.left = self._insert(node.left, key)
        elif key > node.key:
            node.right = self._insert(node.right, key)
        # if key == node.key, ignore duplicates
        return node

    # ---------- Search ----------
    def search(self, key: int) -> bool:
        return self._search(self.root, key)

    def _search(self, node: Optional[Node], key: int) -> bool:
        if node is None:
            return False
        if key == node.key:
            return True
        if key < node.key:
            return self._search(node.left, key)
        return self._search(node.right, key)

    # ---------- Delete ----------
    def delete(self, key: int) -> None:
        self.root = self._delete(self.root, key)

    def _delete(self, node: Optional[Node], key: int) -> Optional[Node]:
        if node is None:
            return None

        if key < node.key:
            node.left = self._delete(node.left, key)
        elif key > node.key:
            node.right = self._delete(node.right, key)
        else:
            # Node found — handle 3 cases
            if node.left is None:
                return node.right
            if node.right is None:
                return node.left
            # Two children: replace with in-order successor (smallest in right subtree)
            successor = self._min_node(node.right)
            node.key = successor.key
            node.right = self._delete(node.right, successor.key)

        return node

    # ---------- Min / Max ----------
    def find_min(self) -> Optional[int]:
        if self.root is None:
            return None
        return self._min_node(self.root).key

    def _min_node(self, node: Node) -> Node:
        while node.left is not None:
            node = node.left
        return node

    def find_max(self) -> Optional[int]:
        if self.root is None:
            return None
        node = self.root
        while node.right is not None:
            node = node.right
        return node.key

    # ---------- Height ----------
    def height(self) -> int:
        return self._height(self.root)

    def _height(self, node: Optional[Node]) -> int:
        if node is None:
            return -1
        return 1 + max(self._height(node.left), self._height(node.right))

    # ---------- Traversals ----------
    def inorder(self) -> List[int]:
        result: List[int] = []
        self._inorder(self.root, result)
        return result

    def _inorder(self, node: Optional[Node], result: List[int]) -> None:
        if node:
            self._inorder(node.left, result)
            result.append(node.key)
            self._inorder(node.right, result)

    def preorder(self) -> List[int]:
        result: List[int] = []
        self._preorder(self.root, result)
        return result

    def _preorder(self, node: Optional[Node], result: List[int]) -> None:
        if node:
            result.append(node.key)
            self._preorder(node.left, result)
            self._preorder(node.right, result)

    def postorder(self) -> List[int]:
        result: List[int] = []
        self._postorder(self.root, result)
        return result

    def _postorder(self, node: Optional[Node], result: List[int]) -> None:
        if node:
            self._postorder(node.left, result)
            self._postorder(node.right, result)
            result.append(node.key)


# ---------- Demo / Manual Test ----------
if __name__ == "__main__":
    bst = BinarySearchTree()
    values = [50, 30, 70, 20, 40, 60, 80, 10]

    for v in values:
        bst.insert(v)

    print("In-order traversal (should be sorted):", bst.inorder())
    print("Pre-order traversal:", bst.preorder())
    print("Post-order traversal:", bst.postorder())
    print("Tree height:", bst.height())
    print("Min value:", bst.find_min())
    print("Max value:", bst.find_max())

    print("\nSearch 40:", bst.search(40))
    print("Search 99:", bst.search(99))

    print("\nDeleting 30...")
    bst.delete(30)
    print("In-order after deletion:", bst.inorder())
