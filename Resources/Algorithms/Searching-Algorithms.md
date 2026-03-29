# Searching Algorithms

A reference for three core searching algorithms used in interviews and real-world systems. Each entry includes a plain-English explanation, pseudocode, Python implementation, and Big-O complexity analysis.

## Table of Contents

- [Binary Search](#binary-search)
- [Breadth-First Search (BFS)](#breadth-first-search-bfs)
- [Depth-First Search (DFS)](#depth-first-search-dfs)

---

## Binary Search

**Category:** Searching
**Time Complexity:** O(log n)
**Space Complexity:** O(1) iterative; O(log n) recursive (call stack)

### Explanation

Binary Search finds a target value in a **sorted** array by repeatedly halving the search space. It starts by comparing the target to the middle element:

- If the target equals the middle element, the search is done.
- If the target is less than the middle, search the left half.
- If the target is greater than the middle, search the right half.

Each comparison eliminates half the remaining elements, giving O(log n) time. The critical requirement is that the input array must be sorted. Binary Search is one of the most important algorithms to know for technical interviews.

### Pseudocode

```text
procedure binarySearch(arr, target):
    low = 0
    high = length of arr - 1

    while low <= high:
        mid = (low + high) / 2

        if arr[mid] == target:
            return mid
        else if arr[mid] < target:
            low = mid + 1
        else:
            high = mid - 1

    return -1  // target not found
```

### Implementation

```python
def binary_search(arr, target):
    """
    Iterative binary search.
    Returns the index of target in arr, or -1 if not found.
    Requires arr to be sorted in ascending order.
    """
    low, high = 0, len(arr) - 1

    while low <= high:
        mid = (low + high) // 2

        if arr[mid] == target:
            return mid
        elif arr[mid] < target:
            low = mid + 1
        else:
            high = mid - 1

    return -1


def binary_search_recursive(arr, target, low=0, high=None):
    """Recursive variant of binary search."""
    if high is None:
        high = len(arr) - 1

    if low > high:
        return -1

    mid = (low + high) // 2

    if arr[mid] == target:
        return mid
    elif arr[mid] < target:
        return binary_search_recursive(arr, target, mid + 1, high)
    else:
        return binary_search_recursive(arr, target, low, mid - 1)


# Example usage
if __name__ == "__main__":
    data = [2, 3, 4, 10, 40, 55, 78]
    target = 10

    result = binary_search(data, target)
    if result != -1:
        print(f"Element {target} found at index {result}")
    else:
        print("Element not found")
    # Output: Element 10 found at index 3
```

---

## Breadth-First Search (BFS)

**Category:** Searching / Graph Traversal
**Time Complexity:** O(V + E) where V = vertices, E = edges
**Space Complexity:** O(V)

### Explanation

Breadth-First Search explores a graph or tree level by level, starting from a source node. It visits all neighbors of the current node before moving to the next level. BFS uses a **queue** (FIFO) to track which nodes to visit next.

BFS is ideal when you need to find the **shortest path** in an unweighted graph, since it always explores the closest nodes first. It guarantees that the first time it reaches a node, it has found the shortest path to that node.

Common applications:
- Shortest path in unweighted graphs
- Level-order traversal of trees
- Finding connected components
- Web crawlers

### Pseudocode

```text
procedure BFS(graph, start):
    visited = empty set
    queue = [start]
    add start to visited

    while queue is not empty:
        node = dequeue from queue
        process node

        for each neighbor of node in graph:
            if neighbor not in visited:
                add neighbor to visited
                enqueue neighbor to queue
```

### Implementation

```python
from collections import deque


def bfs(graph, start):
    """
    Breadth-First Search traversal of a graph.
    graph: dict mapping each node to a list of its neighbors
    start: the starting node
    Returns a list of nodes in BFS visit order.
    """
    visited = set()
    queue = deque([start])
    visited.add(start)
    order = []

    while queue:
        node = queue.popleft()
        order.append(node)

        for neighbor in graph[node]:
            if neighbor not in visited:
                visited.add(neighbor)
                queue.append(neighbor)

    return order


def bfs_shortest_path(graph, start, goal):
    """
    BFS to find the shortest path between start and goal.
    Returns the path as a list of nodes, or None if no path exists.
    """
    if start == goal:
        return [start]

    visited = {start}
    queue = deque([[start]])  # Queue of paths

    while queue:
        path = queue.popleft()
        node = path[-1]

        for neighbor in graph[node]:
            if neighbor == goal:
                return path + [neighbor]
            if neighbor not in visited:
                visited.add(neighbor)
                queue.append(path + [neighbor])

    return None  # No path found


# Example usage
if __name__ == "__main__":
    graph = {
        'A': ['B', 'C'],
        'B': ['A', 'D', 'E'],
        'C': ['A', 'F'],
        'D': ['B'],
        'E': ['B', 'F'],
        'F': ['C', 'E']
    }

    print("BFS order:", bfs(graph, 'A'))
    # Output: BFS order: ['A', 'B', 'C', 'D', 'E', 'F']

    print("Shortest path A -> F:", bfs_shortest_path(graph, 'A', 'F'))
    # Output: Shortest path A -> F: ['A', 'C', 'F']
```

---

## Depth-First Search (DFS)

**Category:** Searching / Graph Traversal
**Time Complexity:** O(V + E) where V = vertices, E = edges
**Space Complexity:** O(V) — for the visited set and call stack (or explicit stack)

### Explanation

Depth-First Search explores a graph by going as deep as possible along each branch before backtracking. Starting from a source node, it follows one path all the way to a dead end, then backtracks and tries the next unvisited path.

DFS can be implemented recursively (using the call stack) or iteratively (using an explicit stack). Unlike BFS, DFS does not guarantee the shortest path, but it uses less memory in sparse graphs and is well-suited for problems that require exploring all possibilities.

Common applications:
- Detecting cycles in a graph
- Topological sorting
- Solving mazes and puzzles
- Finding connected components
- Tree traversals (pre-order, in-order, post-order)

### Pseudocode

```text
// Recursive DFS
procedure DFS(graph, node, visited):
    add node to visited
    process node

    for each neighbor of node in graph:
        if neighbor not in visited:
            DFS(graph, neighbor, visited)

// Iterative DFS
procedure DFS_iterative(graph, start):
    visited = empty set
    stack = [start]

    while stack is not empty:
        node = pop from stack
        if node not in visited:
            add node to visited
            process node
            for each neighbor of node:
                if neighbor not in visited:
                    push neighbor to stack
```

### Implementation

```python
def dfs_recursive(graph, node, visited=None):
    """
    Recursive Depth-First Search traversal.
    graph: dict mapping each node to a list of its neighbors
    Returns a list of nodes in DFS visit order.
    """
    if visited is None:
        visited = set()

    visited.add(node)
    order = [node]

    for neighbor in graph[node]:
        if neighbor not in visited:
            order.extend(dfs_recursive(graph, neighbor, visited))

    return order


def dfs_iterative(graph, start):
    """
    Iterative Depth-First Search using an explicit stack.
    Returns a list of nodes in DFS visit order.
    """
    visited = set()
    stack = [start]
    order = []

    while stack:
        node = stack.pop()
        if node not in visited:
            visited.add(node)
            order.append(node)
            # Push neighbors in reverse order to maintain left-to-right traversal
            for neighbor in reversed(graph[node]):
                if neighbor not in visited:
                    stack.append(neighbor)

    return order


def dfs_has_path(graph, start, goal, visited=None):
    """
    DFS to check if a path exists between start and goal.
    Returns True if a path exists, False otherwise.
    """
    if visited is None:
        visited = set()

    if start == goal:
        return True

    visited.add(start)

    for neighbor in graph[start]:
        if neighbor not in visited:
            if dfs_has_path(graph, neighbor, goal, visited):
                return True

    return False


# Example usage
if __name__ == "__main__":
    graph = {
        'A': ['B', 'C'],
        'B': ['A', 'D', 'E'],
        'C': ['A', 'F'],
        'D': ['B'],
        'E': ['B', 'F'],
        'F': ['C', 'E']
    }

    print("DFS recursive:", dfs_recursive(graph, 'A'))
    # Output: DFS recursive: ['A', 'B', 'D', 'E', 'F', 'C']

    print("DFS iterative:", dfs_iterative(graph, 'A'))
    # Output: DFS iterative: ['A', 'B', 'D', 'E', 'F', 'C']

    print("Path A -> F exists:", dfs_has_path(graph, 'A', 'F'))
    # Output: Path A -> F exists: True
```

---

## Complexity Summary

| Algorithm     | Time Complexity | Space Complexity | Requires Sorted Input | Finds Shortest Path |
|---------------|-----------------|------------------|-----------------------|---------------------|
| Binary Search | O(log n)        | O(1) iterative   | Yes                   | N/A                 |
| BFS           | O(V + E)        | O(V)             | No                    | Yes (unweighted)    |
| DFS           | O(V + E)        | O(V)             | No                    | No                  |
