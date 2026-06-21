# Graph Algorithms

A Python implementation of a weighted graph (adjacency list) with BFS, DFS, and Dijkstra's shortest path algorithm.

## Operations Implemented

- `add_node(node)` / `add_edge(u, v, weight)` — build the graph
- `bfs(start)` — breadth-first traversal, returns visit order
- `dfs(start)` — depth-first traversal (recursive)
- `dfs_iterative(start)` — depth-first traversal using an explicit stack (avoids recursion limits)
- `dijkstra(start)` — shortest distance from `start` to every reachable node
- `shortest_path(start, end)` — reconstructs the actual shortest path between two nodes

## Complexity

| Algorithm | Time Complexity |
|---|---|
| BFS | O(V + E) |
| DFS | O(V + E) |
| Dijkstra (min-heap) | O((V + E) log V) |

Where V = number of vertices, E = number of edges.

## Run it

```bash
python3 graph_algorithms.py
```

Builds a small weighted graph and prints BFS/DFS traversal orders, Dijkstra distances from a source node, and the reconstructed shortest path between two nodes.

## Possible Extensions

- Add A* search (Dijkstra + heuristic) for pathfinding use cases
- Add cycle detection and topological sort for directed graphs
- Add Bellman-Ford to support negative edge weights
- Add unit tests with `pytest`
