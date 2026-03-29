# Data Structures Reference

A reference for seven fundamental data structures. Each entry covers what it is, when to use it, and includes a Python code example.

## Table of Contents

- [Arrays](#arrays)
- [Linked Lists](#linked-lists)
- [Stacks](#stacks)
- [Queues](#queues)
- [Trees](#trees)
- [Graphs](#graphs)
- [Hash Maps](#hash-maps)

---

## Arrays

### Explanation

An array is a collection of elements stored in contiguous memory locations, all of the same type. Elements are accessed by their index in O(1) time. In Python, the built-in `list` serves as a dynamic array — it can grow and shrink automatically, unlike fixed-size arrays in languages like C or Java.

Arrays are the most fundamental data structure and underpin many others (heaps, hash tables, etc.).

**Key operations and complexity:**

| Operation        | Time Complexity |
|------------------|-----------------|
| Access by index  | O(1)            |
| Search (unsorted)| O(n)            |
| Search (sorted)  | O(log n)        |
| Insert at end    | O(1) amortized  |
| Insert at index  | O(n)            |
| Delete at end    | O(1)            |
| Delete at index  | O(n)            |

### Use Cases

- Storing ordered collections of items (e.g., a list of scores, pixels in an image)
- Implementing other data structures (stacks, queues, heaps)
- Matrix and grid representations
- Sliding window and two-pointer algorithms
- Any situation where fast random access by index is needed

### Code Example

```python
# Basic array (Python list) operations
arr = [10, 20, 30, 40, 50]

# Access by index — O(1)
print(arr[2])          # 30
print(arr[-1])         # 50 (last element)

# Append to end — O(1) amortized
arr.append(60)
print(arr)             # [10, 20, 30, 40, 50, 60]

# Insert at index — O(n)
arr.insert(2, 25)
print(arr)             # [10, 20, 25, 30, 40, 50, 60]

# Delete by index — O(n)
arr.pop(2)
print(arr)             # [10, 20, 30, 40, 50, 60]

# Slice — O(k) where k is slice length
print(arr[1:4])        # [20, 30, 40]

# Two-pointer technique example: check if array has a pair summing to target
def has_pair_with_sum(arr, target):
    left, right = 0, len(arr) - 1
    arr.sort()
    while left < right:
        total = arr[left] + arr[right]
        if total == target:
            return True
        elif total < target:
            left += 1
        else:
            right -= 1
    return False

print(has_pair_with_sum([1, 4, 7, 2, 9], 11))  # True (2 + 9)
```

---

## Linked Lists

### Explanation

A linked list is a sequence of nodes where each node stores a value and a pointer (reference) to the next node. Unlike arrays, nodes are not stored in contiguous memory — they are connected by pointers.

There are several variants:
- **Singly linked list** — Each node points to the next node only.
- **Doubly linked list** — Each node points to both the next and previous nodes.
- **Circular linked list** — The last node points back to the first.

Linked lists excel at insertions and deletions at the head or tail (O(1) with a tail pointer), but random access requires traversal from the head — O(n).

**Key operations and complexity (singly linked):**

| Operation          | Time Complexity |
|--------------------|-----------------|
| Access by index    | O(n)            |
| Search             | O(n)            |
| Insert at head     | O(1)            |
| Insert at tail     | O(1) with tail  |
| Insert at index    | O(n)            |
| Delete at head     | O(1)            |
| Delete at tail     | O(n) singly     |

### Use Cases

- Implementing stacks and queues
- Situations with frequent insertions/deletions at the beginning
- Implementing LRU (Least Recently Used) caches
- Representing polynomials or sparse matrices
- Undo/redo functionality (doubly linked)

### Code Example

```python
class Node:
    def __init__(self, value):
        self.value = value
        self.next = None


class LinkedList:
    def __init__(self):
        self.head = None
        self.size = 0

    def append(self, value):
        """Add to end — O(n) without tail pointer."""
        new_node = Node(value)
        if not self.head:
            self.head = new_node
        else:
            current = self.head
            while current.next:
                current = current.next
            current.next = new_node
        self.size += 1

    def prepend(self, value):
        """Add to front — O(1)."""
        new_node = Node(value)
        new_node.next = self.head
        self.head = new_node
        self.size += 1

    def delete(self, value):
        """Remove first occurrence of value — O(n)."""
        if not self.head:
            return
        if self.head.value == value:
            self.head = self.head.next
            self.size -= 1
            return
        current = self.head
        while current.next:
            if current.next.value == value:
                current.next = current.next.next
                self.size -= 1
                return
            current = current.next

    def to_list(self):
        """Convert to Python list for display."""
        result = []
        current = self.head
        while current:
            result.append(current.value)
            current = current.next
        return result

    def reverse(self):
        """Reverse the linked list in-place — O(n)."""
        prev = None
        current = self.head
        while current:
            next_node = current.next
            current.next = prev
            prev = current
            current = next_node
        self.head = prev


# Example usage
ll = LinkedList()
ll.append(1)
ll.append(2)
ll.append(3)
ll.prepend(0)
print(ll.to_list())   # [0, 1, 2, 3]

ll.delete(2)
print(ll.to_list())   # [0, 1, 3]

ll.reverse()
print(ll.to_list())   # [3, 1, 0]
```

---

## Stacks

### Explanation

A stack is a linear data structure that follows the **LIFO** (Last In, First Out) principle — the last element added is the first one removed. Think of a stack of plates: you add to the top and remove from the top.

The two primary operations are:
- **Push** — Add an element to the top.
- **Pop** — Remove and return the top element.

Both operations are O(1). In Python, a `list` works perfectly as a stack using `append()` and `pop()`.

**Key operations and complexity:**

| Operation | Time Complexity |
|-----------|-----------------|
| Push      | O(1)            |
| Pop       | O(1)            |
| Peek/Top  | O(1)            |
| Search    | O(n)            |

### Use Cases

- Function call management (the call stack)
- Undo/redo operations in editors
- Parsing expressions and matching brackets
- Backtracking algorithms (DFS, maze solving)
- Browser history (back button)
- Evaluating postfix/prefix expressions

### Code Example

```python
# Using Python list as a stack
stack = []

# Push — O(1)
stack.append(1)
stack.append(2)
stack.append(3)
print(stack)          # [1, 2, 3]

# Peek — O(1)
print(stack[-1])      # 3 (top element)

# Pop — O(1)
print(stack.pop())    # 3
print(stack)          # [1, 2]

# Check if empty
print(len(stack) == 0)  # False


# Practical example: check balanced brackets
def is_balanced(s):
    """Returns True if all brackets in s are properly balanced."""
    stack = []
    matching = {')': '(', ']': '[', '}': '{'}

    for char in s:
        if char in '([{':
            stack.append(char)
        elif char in ')]}':
            if not stack or stack[-1] != matching[char]:
                return False
            stack.pop()

    return len(stack) == 0


print(is_balanced("({[]})"))   # True
print(is_balanced("({[})"))    # False
print(is_balanced("((()))"))   # True


# Stack class with explicit interface
class Stack:
    def __init__(self):
        self._data = []

    def push(self, item):
        self._data.append(item)

    def pop(self):
        if self.is_empty():
            raise IndexError("Pop from empty stack")
        return self._data.pop()

    def peek(self):
        if self.is_empty():
            raise IndexError("Peek at empty stack")
        return self._data[-1]

    def is_empty(self):
        return len(self._data) == 0

    def size(self):
        return len(self._data)
```

---

## Queues

### Explanation

A queue is a linear data structure that follows the **FIFO** (First In, First Out) principle — the first element added is the first one removed. Think of a line at a checkout: people join at the back and leave from the front.

The two primary operations are:
- **Enqueue** — Add an element to the back.
- **Dequeue** — Remove and return the front element.

In Python, use `collections.deque` for an efficient queue — it provides O(1) appends and pops from both ends, unlike a list which has O(n) `pop(0)`.

**Key operations and complexity:**

| Operation | Time Complexity |
|-----------|-----------------|
| Enqueue   | O(1)            |
| Dequeue   | O(1)            |
| Peek      | O(1)            |
| Search    | O(n)            |

### Use Cases

- BFS (Breadth-First Search) traversal
- Task scheduling and job queues
- Print spoolers and request buffers
- Level-order tree traversal
- Sliding window problems
- Producer-consumer patterns

### Code Example

```python
from collections import deque

# Using deque as a queue
queue = deque()

# Enqueue — O(1)
queue.append(1)
queue.append(2)
queue.append(3)
print(queue)              # deque([1, 2, 3])

# Peek front — O(1)
print(queue[0])           # 1

# Dequeue — O(1)
print(queue.popleft())    # 1
print(queue)              # deque([2, 3])


# Queue class with explicit interface
class Queue:
    def __init__(self):
        self._data = deque()

    def enqueue(self, item):
        self._data.append(item)

    def dequeue(self):
        if self.is_empty():
            raise IndexError("Dequeue from empty queue")
        return self._data.popleft()

    def peek(self):
        if self.is_empty():
            raise IndexError("Peek at empty queue")
        return self._data[0]

    def is_empty(self):
        return len(self._data) == 0

    def size(self):
        return len(self._data)


# Practical example: level-order tree traversal using a queue
class TreeNode:
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None


def level_order(root):
    """Returns nodes level by level using BFS."""
    if not root:
        return []

    result = []
    queue = deque([root])

    while queue:
        level_size = len(queue)
        level = []
        for _ in range(level_size):
            node = queue.popleft()
            level.append(node.val)
            if node.left:
                queue.append(node.left)
            if node.right:
                queue.append(node.right)
        result.append(level)

    return result


# Build a simple tree:    1
#                        / \
#                       2   3
#                      / \
#                     4   5
root = TreeNode(1)
root.left = TreeNode(2)
root.right = TreeNode(3)
root.left.left = TreeNode(4)
root.left.right = TreeNode(5)

print(level_order(root))  # [[1], [2, 3], [4, 5]]
```

---

## Trees

### Explanation

A tree is a hierarchical data structure consisting of nodes connected by edges. Every tree has a **root** node at the top, and each node can have zero or more **children**. Nodes with no children are called **leaves**.

Key terminology:
- **Root** — The topmost node (no parent)
- **Parent / Child** — Directional relationship between connected nodes
- **Height** — Longest path from root to a leaf
- **Depth** — Distance from the root to a given node

The most common variant is the **Binary Tree**, where each node has at most two children (left and right). A **Binary Search Tree (BST)** adds the constraint that left child < parent < right child, enabling O(log n) search on balanced trees.

**BST key operations (balanced):**

| Operation | Time Complexity |
|-----------|-----------------|
| Search    | O(log n)        |
| Insert    | O(log n)        |
| Delete    | O(log n)        |
| Traversal | O(n)            |

### Use Cases

- File system directory structures
- HTML/XML DOM representation
- Database indexing (B-trees)
- Expression parsing (abstract syntax trees)
- Priority queues (heaps are complete binary trees)
- Autocomplete and prefix search (tries)

### Code Example

```python
class TreeNode:
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None


class BinarySearchTree:
    def __init__(self):
        self.root = None

    def insert(self, val):
        """Insert a value into the BST — O(log n) average."""
        self.root = self._insert(self.root, val)

    def _insert(self, node, val):
        if node is None:
            return TreeNode(val)
        if val < node.val:
            node.left = self._insert(node.left, val)
        elif val > node.val:
            node.right = self._insert(node.right, val)
        return node  # Duplicate values are ignored

    def search(self, val):
        """Search for a value — O(log n) average."""
        return self._search(self.root, val)

    def _search(self, node, val):
        if node is None:
            return False
        if val == node.val:
            return True
        elif val < node.val:
            return self._search(node.left, val)
        else:
            return self._search(node.right, val)

    def inorder(self):
        """In-order traversal returns sorted values — O(n)."""
        result = []
        self._inorder(self.root, result)
        return result

    def _inorder(self, node, result):
        if node:
            self._inorder(node.left, result)
            result.append(node.val)
            self._inorder(node.right, result)


# Example usage
bst = BinarySearchTree()
for val in [5, 3, 7, 1, 4, 6, 8]:
    bst.insert(val)

print("In-order (sorted):", bst.inorder())  # [1, 3, 4, 5, 6, 7, 8]
print("Search 4:", bst.search(4))            # True
print("Search 9:", bst.search(9))            # False
```

---

## Graphs

### Explanation

A graph is a collection of **nodes** (vertices) connected by **edges**. Unlike trees, graphs can have cycles, multiple paths between nodes, and disconnected components.

Graphs can be:
- **Directed** — Edges have a direction (A → B does not imply B → A)
- **Undirected** — Edges are bidirectional
- **Weighted** — Edges have associated costs or distances
- **Unweighted** — All edges are equal

Common representations:
- **Adjacency list** — A dictionary mapping each node to its list of neighbors. Space-efficient for sparse graphs.
- **Adjacency matrix** — A 2D array where `matrix[i][j] = 1` if there is an edge. Fast edge lookup but O(V²) space.

**Key operations:**

| Operation          | Adjacency List | Adjacency Matrix |
|--------------------|----------------|------------------|
| Add vertex         | O(1)           | O(V²)            |
| Add edge           | O(1)           | O(1)             |
| Check edge exists  | O(degree)      | O(1)             |
| Get all neighbors  | O(degree)      | O(V)             |
| Space              | O(V + E)       | O(V²)            |

### Use Cases

- Social networks (users as nodes, friendships as edges)
- Maps and navigation (cities as nodes, roads as edges)
- Dependency resolution (package managers, build systems)
- Web page link analysis (PageRank)
- Network routing protocols
- Recommendation systems

### Code Example

```python
from collections import defaultdict, deque


class Graph:
    def __init__(self, directed=False):
        self.adjacency_list = defaultdict(list)
        self.directed = directed

    def add_edge(self, u, v, weight=None):
        """Add an edge between u and v."""
        self.adjacency_list[u].append(v)
        if not self.directed:
            self.adjacency_list[v].append(u)

    def neighbors(self, node):
        return self.adjacency_list[node]

    def bfs(self, start):
        """Breadth-First Search from start node."""
        visited = set([start])
        queue = deque([start])
        order = []

        while queue:
            node = queue.popleft()
            order.append(node)
            for neighbor in self.adjacency_list[node]:
                if neighbor not in visited:
                    visited.add(neighbor)
                    queue.append(neighbor)
        return order

    def dfs(self, start, visited=None):
        """Depth-First Search from start node."""
        if visited is None:
            visited = set()
        visited.add(start)
        order = [start]
        for neighbor in self.adjacency_list[start]:
            if neighbor not in visited:
                order.extend(self.dfs(neighbor, visited))
        return order

    def has_cycle_undirected(self):
        """Detect cycle in an undirected graph using DFS."""
        visited = set()

        def dfs_cycle(node, parent):
            visited.add(node)
            for neighbor in self.adjacency_list[node]:
                if neighbor not in visited:
                    if dfs_cycle(neighbor, node):
                        return True
                elif neighbor != parent:
                    return True
            return False

        for node in self.adjacency_list:
            if node not in visited:
                if dfs_cycle(node, None):
                    return True
        return False


# Example usage
g = Graph(directed=False)
g.add_edge('A', 'B')
g.add_edge('A', 'C')
g.add_edge('B', 'D')
g.add_edge('C', 'D')
g.add_edge('D', 'E')

print("BFS from A:", g.bfs('A'))   # ['A', 'B', 'C', 'D', 'E']
print("DFS from A:", g.dfs('A'))   # ['A', 'B', 'D', 'C', 'E'] (order may vary)
print("Has cycle:", g.has_cycle_undirected())  # True (A-B-D-C-A)
```

---

## Hash Maps

### Explanation

A hash map (also called a hash table or dictionary) stores key-value pairs and provides average O(1) time for insertions, lookups, and deletions. It works by applying a **hash function** to the key to compute an index into an underlying array (called a bucket). The value is stored at that index.

**Collisions** occur when two keys hash to the same index. Common resolution strategies:
- **Chaining** — Each bucket holds a linked list of entries.
- **Open addressing** — Probe for the next available slot.

In Python, the built-in `dict` is a highly optimized hash map.

**Key operations and complexity (average case):**

| Operation | Time Complexity |
|-----------|-----------------|
| Insert    | O(1)            |
| Lookup    | O(1)            |
| Delete    | O(1)            |
| Search    | O(1)            |
| Worst case (all collisions) | O(n) |

### Use Cases

- Counting frequencies (word count, character count)
- Caching and memoization
- Implementing sets
- Grouping/indexing data by a key
- Two-sum and similar lookup problems
- Deduplication

### Code Example

```python
# Python dict as a hash map
phone_book = {}

# Insert — O(1)
phone_book["Alice"] = "555-1234"
phone_book["Bob"] = "555-5678"
phone_book["Carol"] = "555-9012"

# Lookup — O(1)
print(phone_book["Alice"])          # 555-1234
print(phone_book.get("Dave", "Not found"))  # Not found

# Delete — O(1)
del phone_book["Bob"]
print(phone_book)                   # {'Alice': '555-1234', 'Carol': '555-9012'}

# Check existence — O(1)
print("Alice" in phone_book)        # True
print("Bob" in phone_book)          # False

# Iterate
for name, number in phone_book.items():
    print(f"{name}: {number}")


# Practical example 1: frequency counter
def char_frequency(s):
    freq = {}
    for char in s:
        freq[char] = freq.get(char, 0) + 1
    return freq

print(char_frequency("hello"))  # {'h': 1, 'e': 1, 'l': 2, 'o': 1}


# Practical example 2: two-sum problem
def two_sum(nums, target):
    """
    Find indices of two numbers that add up to target.
    Returns a tuple of indices, or None if no solution.
    O(n) time using a hash map.
    """
    seen = {}  # value -> index
    for i, num in enumerate(nums):
        complement = target - num
        if complement in seen:
            return (seen[complement], i)
        seen[num] = i
    return None

print(two_sum([2, 7, 11, 15], 9))   # (0, 1)  — 2 + 7 = 9
print(two_sum([3, 2, 4], 6))        # (1, 2)  — 2 + 4 = 6


# Practical example 3: group anagrams
def group_anagrams(words):
    """Group words that are anagrams of each other."""
    groups = {}
    for word in words:
        key = tuple(sorted(word))  # Canonical form
        groups.setdefault(key, []).append(word)
    return list(groups.values())

print(group_anagrams(["eat", "tea", "tan", "ate", "nat", "bat"]))
# [['eat', 'tea', 'ate'], ['tan', 'nat'], ['bat']]
```

---

## Complexity Summary

| Data Structure | Access  | Search  | Insert  | Delete  | Space  |
|----------------|---------|---------|---------|---------|--------|
| Array          | O(1)    | O(n)    | O(n)    | O(n)    | O(n)   |
| Linked List    | O(n)    | O(n)    | O(1)*   | O(1)*   | O(n)   |
| Stack          | O(n)    | O(n)    | O(1)    | O(1)    | O(n)   |
| Queue          | O(n)    | O(n)    | O(1)    | O(1)    | O(n)   |
| BST (balanced) | O(log n)| O(log n)| O(log n)| O(log n)| O(n)   |
| Graph          | O(1)    | O(V+E)  | O(1)    | O(V+E)  | O(V+E) |
| Hash Map       | O(1)    | O(1)    | O(1)    | O(1)    | O(n)   |

*Linked list insert/delete is O(1) when you already have a reference to the node; O(n) to find the node first.
