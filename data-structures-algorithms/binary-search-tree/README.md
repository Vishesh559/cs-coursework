# Binary Search Tree (BST)

A Python implementation of a Binary Search Tree with full CRUD operations and traversals.

## Operations Implemented

- `insert(key)` — insert a value, O(log n) average / O(n) worst case
- `search(key)` — check if a value exists
- `delete(key)` — delete a value, handling 0, 1, and 2-child node cases via in-order successor replacement
- `find_min()` / `find_max()` — retrieve smallest/largest value
- `height()` — compute tree height
- `inorder()` / `preorder()` / `postorder()` — traversal methods

## Complexity

| Operation | Average | Worst Case |
|---|---|---|
| Insert | O(log n) | O(n) |
| Search | O(log n) | O(n) |
| Delete | O(log n) | O(n) |

Worst case occurs when the tree becomes skewed (e.g., inserting sorted data), degrading to a linked list.

## Run it

```bash
python3 bst.py
```

This runs a demo that builds a tree, prints all three traversals, computes height/min/max, and demonstrates deletion.

## Possible Extensions

- Add self-balancing (AVL or Red-Black tree) to guarantee O(log n) worst case
- Add iterative (non-recursive) versions of each method
- Add unit tests with `pytest`
