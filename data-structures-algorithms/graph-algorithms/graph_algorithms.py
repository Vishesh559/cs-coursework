"""
Graph Algorithms Implementation
--------------------------------
Implements a simple weighted/unweighted graph using an adjacency list,
with BFS, DFS, and Dijkstra's shortest path algorithm.

Time Complexity:
- BFS / DFS: O(V + E)
- Dijkstra (with min-heap): O((V + E) log V)
"""

import heapq
from collections import deque
from typing import Dict, List, Tuple, Optional


class Graph:
    def __init__(self, directed: bool = False):
        self.directed = directed
        self.adjacency: Dict[str, List[Tuple[str, int]]] = {}

    def add_node(self, node: str) -> None:
        if node not in self.adjacency:
            self.adjacency[node] = []

    def add_edge(self, u: str, v: str, weight: int = 1) -> None:
        self.add_node(u)
        self.add_node(v)
        self.adjacency[u].append((v, weight))
        if not self.directed:
            self.adjacency[v].append((u, weight))

    # ---------- BFS ----------
    def bfs(self, start: str) -> List[str]:
        """Returns nodes in the order they're visited (level by level)."""
        visited = {start}
        order = []
        queue = deque([start])

        while queue:
            node = queue.popleft()
            order.append(node)
            for neighbor, _ in self.adjacency.get(node, []):
                if neighbor not in visited:
                    visited.add(neighbor)
                    queue.append(neighbor)

        return order

    # ---------- DFS ----------
    def dfs(self, start: str) -> List[str]:
        """Returns nodes in the order they're visited (depth-first)."""
        visited = set()
        order = []

        def _dfs(node: str) -> None:
            visited.add(node)
            order.append(node)
            for neighbor, _ in self.adjacency.get(node, []):
                if neighbor not in visited:
                    _dfs(neighbor)

        _dfs(start)
        return order

    def dfs_iterative(self, start: str) -> List[str]:
        """Stack-based DFS, avoids recursion depth limits on large graphs."""
        visited = set()
        order = []
        stack = [start]

        while stack:
            node = stack.pop()
            if node not in visited:
                visited.add(node)
                order.append(node)
                # reversed so traversal order matches recursive DFS roughly
                for neighbor, _ in reversed(self.adjacency.get(node, [])):
                    if neighbor not in visited:
                        stack.append(neighbor)

        return order

    # ---------- Dijkstra's Shortest Path ----------
    def dijkstra(self, start: str) -> Dict[str, float]:
        """Returns shortest distance from start to every reachable node."""
        distances: Dict[str, float] = {node: float("inf") for node in self.adjacency}
        distances[start] = 0
        visited = set()
        # min-heap of (distance, node)
        heap = [(0, start)]

        while heap:
            current_dist, node = heapq.heappop(heap)

            if node in visited:
                continue
            visited.add(node)

            for neighbor, weight in self.adjacency.get(node, []):
                distance = current_dist + weight
                if distance < distances[neighbor]:
                    distances[neighbor] = distance
                    heapq.heappush(heap, (distance, neighbor))

        return distances

    def shortest_path(self, start: str, end: str) -> Optional[List[str]]:
        """Returns the actual shortest path (list of nodes) from start to end."""
        distances: Dict[str, float] = {node: float("inf") for node in self.adjacency}
        previous: Dict[str, Optional[str]] = {node: None for node in self.adjacency}
        distances[start] = 0
        heap = [(0, start)]
        visited = set()

        while heap:
            current_dist, node = heapq.heappop(heap)
            if node in visited:
                continue
            visited.add(node)

            if node == end:
                break

            for neighbor, weight in self.adjacency.get(node, []):
                distance = current_dist + weight
                if distance < distances[neighbor]:
                    distances[neighbor] = distance
                    previous[neighbor] = node
                    heapq.heappush(heap, (distance, neighbor))

        if distances[end] == float("inf"):
            return None  # unreachable

        # reconstruct path by walking back through 'previous'
        path = []
        node: Optional[str] = end
        while node is not None:
            path.append(node)
            node = previous[node]
        path.reverse()
        return path


# ---------- Demo / Manual Test ----------
if __name__ == "__main__":
    g = Graph(directed=False)

    # Build a small weighted graph
    g.add_edge("A", "B", 4)
    g.add_edge("A", "C", 1)
    g.add_edge("C", "B", 2)
    g.add_edge("B", "D", 5)
    g.add_edge("C", "D", 8)
    g.add_edge("D", "E", 3)

    print("BFS from A:", g.bfs("A"))
    print("DFS (recursive) from A:", g.dfs("A"))
    print("DFS (iterative) from A:", g.dfs_iterative("A"))

    print("\nDijkstra shortest distances from A:", g.dijkstra("A"))
    print("Shortest path from A to E:", g.shortest_path("A", "E"))
    print("Shortest path from A to Z (unreachable):", g.shortest_path("A", "Z") if "Z" in g.adjacency else "Z not in graph")
