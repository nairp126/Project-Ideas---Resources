# Big-O Complexity Cheatsheet

A quick reference for time and space complexity of common operations, data structures, and algorithms.

## Table of Contents
- [Big-O Notation Basics](#big-o-notation-basics)
- [Complexity Classes](#complexity-classes)
- [Data Structure Operations](#data-structure-operations)
- [Sorting Algorithms](#sorting-algorithms)
- [Searching Algorithms](#searching-algorithms)
- [Space Complexity](#space-complexity)
- [Complexity Comparison Chart](#complexity-comparison-chart)

---

## Big-O Notation Basics

Big-O notation describes the **upper bound** of an algorithm's growth rate — how runtime or memory usage scales as input size `n` grows. It ignores constants and lower-order terms, focusing on the dominant factor.

```text
# Key rules
1. Drop constants:       O(2n)     → O(n)
2. Drop lower terms:     O(n² + n) → O(n²)
3. Different inputs:     O(a + b)  — keep both if inputs are independent
4. Nested loops:         O(n) × O(n) = O(n²)
```

**Common notations:**

| Notation | Name | Example |
|---|---|---|
| O(1) | Constant | Array index access |
| O(log n) | Logarithmic | Binary search |
| O(n) | Linear | Linear scan |
| O(n log n) | Linearithmic | Merge sort |
| O(n²) | Quadratic | Bubble sort |
| O(2ⁿ) | Exponential | Recursive Fibonacci |
| O(n!) | Factorial | Permutation generation |

---

## Complexity Classes

### O(1) — Constant Time

Runtime does not change regardless of input size.

```python
# Array index access
arr = [1, 2, 3, 4, 5]
first = arr[0]          # O(1)

# Hash map lookup
cache = {"key": "value"}
val = cache["key"]      # O(1)

# Stack push/pop
stack = []
stack.append(42)        # O(1)
stack.pop()             # O(1)
```

### O(log n) — Logarithmic Time

Input is halved at each step. Extremely efficient for large inputs.

```python
# Binary search (iterative)
def binary_search(arr, target):
    lo, hi = 0, len(arr) - 1
    while lo <= hi:
        mid = (lo + hi) // 2
        if arr[mid] == target:
            return mid
        elif arr[mid] < target:
            lo = mid + 1
        else:
            hi = mid - 1
    return -1
# Time: O(log n) | Space: O(1)
```

### O(n) — Linear Time

Runtime grows proportionally with input size.

```python
# Linear scan
def find_max(arr):
    max_val = arr[0]
    for x in arr:           # visits every element once
        if x > max_val:
            max_val = x
    return max_val
# Time: O(n) | Space: O(1)
```

### O(n log n) — Linearithmic Time

Typical of efficient sorting algorithms. Slightly worse than linear but far better than quadratic.

```python
# Merge sort
def merge_sort(arr):
    if len(arr) <= 1:
        return arr
    mid = len(arr) // 2
    left = merge_sort(arr[:mid])
    right = merge_sort(arr[mid:])
    return merge(left, right)
# Time: O(n log n) | Space: O(n)
```

### O(n²) — Quadratic Time

Nested iteration over the input. Acceptable for small inputs, slow for large ones.

```python
# Bubble sort
def bubble_sort(arr):
    n = len(arr)
    for i in range(n):
        for j in range(n - i - 1):   # nested loop → O(n²)
            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]
# Time: O(n²) | Space: O(1)
```

### O(2ⁿ) — Exponential Time

Doubles with each additional input element. Only feasible for very small inputs.

```python
# Naive recursive Fibonacci
def fib(n):
    if n <= 1:
        return n
    return fib(n - 1) + fib(n - 2)   # two recursive calls per level
# Time: O(2ⁿ) | Space: O(n) call stack

# Optimized with memoization → O(n)
from functools import lru_cache

@lru_cache(maxsize=None)
def fib_memo(n):
    if n <= 1:
        return n
    return fib_memo(n - 1) + fib_memo(n - 2)
# Time: O(n) | Space: O(n)
```

### O(n!) — Factorial Time

Generates all permutations. Only practical for n ≤ ~12.

```python
# Generate all permutations
from itertools import permutations

def all_perms(arr):
    return list(permutations(arr))
# Time: O(n!) | Space: O(n!)
```

---

## Data Structure Operations

### Arrays / Lists

| Operation | Average | Worst | Notes |
|---|---|---|---|
| Access by index | O(1) | O(1) | Direct memory offset |
| Search (unsorted) | O(n) | O(n) | Must scan all elements |
| Search (sorted) | O(log n) | O(log n) | Binary search |
| Insert at end | O(1)* | O(n) | *Amortized; resize is O(n) |
| Insert at index | O(n) | O(n) | Shifts elements right |
| Delete at end | O(1) | O(1) | |
| Delete at index | O(n) | O(n) | Shifts elements left |

```python
arr = [1, 2, 3, 4, 5]
arr[2]          # O(1) — access
arr.append(6)   # O(1) amortized — insert at end
arr.insert(0, 0)  # O(n) — insert at front
arr.pop()       # O(1) — delete from end
arr.pop(0)      # O(n) — delete from front
```

### Linked Lists

| Operation | Singly Linked | Doubly Linked | Notes |
|---|---|---|---|
| Access by index | O(n) | O(n) | Must traverse from head |
| Search | O(n) | O(n) | |
| Insert at head | O(1) | O(1) | |
| Insert at tail | O(n) / O(1)* | O(1)* | *O(1) with tail pointer |
| Insert at index | O(n) | O(n) | Traverse to position first |
| Delete at head | O(1) | O(1) | |
| Delete at tail | O(n) | O(1) | Doubly linked has prev pointer |
| Delete at index | O(n) | O(n) | |

### Stacks

| Operation | Time | Notes |
|---|---|---|
| Push | O(1) | Add to top |
| Pop | O(1) | Remove from top |
| Peek / Top | O(1) | View top without removing |
| Search | O(n) | Must pop to find |

```python
stack = []
stack.append(x)   # push  — O(1)
stack.pop()       # pop   — O(1)
stack[-1]         # peek  — O(1)
```

### Queues

| Operation | Time | Notes |
|---|---|---|
| Enqueue | O(1) | Add to rear |
| Dequeue | O(1) | Remove from front |
| Peek | O(1) | View front without removing |
| Search | O(n) | |

```python
from collections import deque

q = deque()
q.append(x)       # enqueue — O(1)
q.popleft()       # dequeue — O(1)
q[0]              # peek    — O(1)
```

### Hash Maps / Dictionaries

| Operation | Average | Worst | Notes |
|---|---|---|---|
| Insert | O(1) | O(n) | Worst case: all keys collide |
| Lookup | O(1) | O(n) | |
| Delete | O(1) | O(n) | |
| Search by value | O(n) | O(n) | Must scan all values |

```python
d = {}
d["key"] = "val"    # insert — O(1) avg
d["key"]            # lookup — O(1) avg
del d["key"]        # delete — O(1) avg
"key" in d          # O(1) avg
```

### Binary Search Trees (BST)

| Operation | Average | Worst | Notes |
|---|---|---|---|
| Search | O(log n) | O(n) | Worst: degenerate (sorted input) |
| Insert | O(log n) | O(n) | |
| Delete | O(log n) | O(n) | |
| Min / Max | O(log n) | O(n) | |
| In-order traversal | O(n) | O(n) | Visits all nodes |

> Balanced BSTs (AVL, Red-Black) guarantee O(log n) for all operations.

### Heaps (Binary Heap)

| Operation | Time | Notes |
|---|---|---|
| Insert | O(log n) | Bubble up |
| Extract min/max | O(log n) | Bubble down |
| Peek min/max | O(1) | Root element |
| Build heap | O(n) | Heapify all nodes |
| Search | O(n) | No ordering guarantee |

```python
import heapq

heap = []
heapq.heappush(heap, 5)    # O(log n)
heapq.heappop(heap)        # O(log n)
heap[0]                    # O(1) — peek min
heapq.heapify(arr)         # O(n) — build from list
```

### Graphs

| Operation | Adjacency List | Adjacency Matrix | Notes |
|---|---|---|---|
| Add vertex | O(1) | O(V²) | Matrix must resize |
| Add edge | O(1) | O(1) | |
| Remove vertex | O(V + E) | O(V²) | |
| Remove edge | O(E) | O(1) | |
| Check edge exists | O(V) | O(1) | |
| BFS / DFS | O(V + E) | O(V²) | |
| Space | O(V + E) | O(V²) | List is sparse-friendly |

> V = number of vertices, E = number of edges.

---

## Sorting Algorithms

| Algorithm | Best | Average | Worst | Space | Stable? |
|---|---|---|---|---|---|
| Bubble Sort | O(n) | O(n²) | O(n²) | O(1) | Yes |
| Selection Sort | O(n²) | O(n²) | O(n²) | O(1) | No |
| Insertion Sort | O(n) | O(n²) | O(n²) | O(1) | Yes |
| Merge Sort | O(n log n) | O(n log n) | O(n log n) | O(n) | Yes |
| Quick Sort | O(n log n) | O(n log n) | O(n²) | O(log n) | No |
| Heap Sort | O(n log n) | O(n log n) | O(n log n) | O(1) | No |
| Counting Sort | O(n + k) | O(n + k) | O(n + k) | O(k) | Yes |
| Radix Sort | O(nk) | O(nk) | O(nk) | O(n + k) | Yes |
| Tim Sort | O(n) | O(n log n) | O(n log n) | O(n) | Yes |

> k = range of input values. Tim Sort is Python's built-in sort.

```python
# Python's built-in sort (Tim Sort) — O(n log n)
arr.sort()              # in-place
sorted_arr = sorted(arr)  # returns new list

# Quick sort (in-place, average O(n log n))
def quicksort(arr, lo, hi):
    if lo < hi:
        pivot = partition(arr, lo, hi)
        quicksort(arr, lo, pivot - 1)
        quicksort(arr, pivot + 1, hi)

# Merge sort (stable, guaranteed O(n log n))
def merge_sort(arr):
    if len(arr) <= 1:
        return arr
    mid = len(arr) // 2
    left = merge_sort(arr[:mid])
    right = merge_sort(arr[mid:])
    return merge(left, right)
```

---

## Searching Algorithms

| Algorithm | Best | Average | Worst | Space | Requirement |
|---|---|---|---|---|---|
| Linear Search | O(1) | O(n) | O(n) | O(1) | None |
| Binary Search | O(1) | O(log n) | O(log n) | O(1) | Sorted array |
| BFS | O(1) | O(V + E) | O(V + E) | O(V) | Graph / tree |
| DFS | O(1) | O(V + E) | O(V + E) | O(V) | Graph / tree |
| Jump Search | O(1) | O(√n) | O(√n) | O(1) | Sorted array |
| Interpolation Search | O(1) | O(log log n) | O(n) | O(1) | Sorted, uniform |

```python
# Linear search — O(n)
def linear_search(arr, target):
    for i, val in enumerate(arr):
        if val == target:
            return i
    return -1

# Binary search — O(log n), requires sorted input
def binary_search(arr, target):
    lo, hi = 0, len(arr) - 1
    while lo <= hi:
        mid = (lo + hi) // 2
        if arr[mid] == target:
            return mid
        elif arr[mid] < target:
            lo = mid + 1
        else:
            hi = mid - 1
    return -1

# BFS — O(V + E), finds shortest path in unweighted graph
from collections import deque

def bfs(graph, start):
    visited = set()
    queue = deque([start])
    visited.add(start)
    while queue:
        node = queue.popleft()
        for neighbor in graph[node]:
            if neighbor not in visited:
                visited.add(neighbor)
                queue.append(neighbor)

# DFS — O(V + E), explores depth-first
def dfs(graph, node, visited=None):
    if visited is None:
        visited = set()
    visited.add(node)
    for neighbor in graph[node]:
        if neighbor not in visited:
            dfs(graph, neighbor, visited)
    return visited
```

---

## Space Complexity

Space complexity measures the total memory an algorithm uses relative to input size `n`. It includes both **auxiliary space** (extra memory used by the algorithm) and **input space**.

### Common Space Complexities

| Complexity | Example |
|---|---|
| O(1) | Iterative binary search, in-place sort |
| O(log n) | Recursive binary search (call stack) |
| O(n) | Storing a copy of the input, hash map |
| O(n log n) | Merge sort auxiliary arrays |
| O(n²) | 2D matrix, adjacency matrix for dense graph |

```python
# O(1) space — no extra memory proportional to n
def sum_array(arr):
    total = 0           # single variable
    for x in arr:
        total += x
    return total

# O(n) space — stores n items
def reverse_array(arr):
    return arr[::-1]    # creates a new list of size n

# O(n) space — recursion call stack depth = n
def factorial(n):
    if n == 0:
        return 1
    return n * factorial(n - 1)   # n frames on the call stack

# O(log n) space — call stack depth = log n
def binary_search_recursive(arr, target, lo, hi):
    if lo > hi:
        return -1
    mid = (lo + hi) // 2
    if arr[mid] == target:
        return mid
    elif arr[mid] < target:
        return binary_search_recursive(arr, target, mid + 1, hi)
    else:
        return binary_search_recursive(arr, target, lo, mid - 1)
```

### Space vs. Time Trade-offs

```text
# Memoization: trade space for time
# Naive Fibonacci:  Time O(2ⁿ), Space O(n)
# Memoized:         Time O(n),   Space O(n)  ← better time, same space

# In-place sort: trade time for space
# Merge sort:    Time O(n log n), Space O(n)
# Heap sort:     Time O(n log n), Space O(1) ← better space, same time

# Hash map lookup: trade space for time
# Linear scan:   Time O(n), Space O(1)
# Hash map:      Time O(1), Space O(n)       ← better time, more space
```

---

## Complexity Comparison Chart

Growth rates from fastest to slowest (for n = 1,000):

| Complexity | n = 10 | n = 100 | n = 1,000 | n = 10,000 |
|---|---|---|---|---|
| O(1) | 1 | 1 | 1 | 1 |
| O(log n) | ~3 | ~7 | ~10 | ~13 |
| O(n) | 10 | 100 | 1,000 | 10,000 |
| O(n log n) | ~33 | ~664 | ~9,966 | ~132,877 |
| O(n²) | 100 | 10,000 | 1,000,000 | 100,000,000 |
| O(2ⁿ) | 1,024 | ~10³⁰ | ~10³⁰¹ | — |
| O(n!) | 3,628,800 | — | — | — |

```text
# Rule of thumb for interview problems:
# n ≤ 10        → O(n!) or O(2ⁿ) acceptable
# n ≤ 20        → O(2ⁿ) acceptable
# n ≤ 100       → O(n³) acceptable
# n ≤ 1,000     → O(n²) acceptable
# n ≤ 100,000   → O(n log n) required
# n ≤ 10,000,000 → O(n) required
# n > 10,000,000 → O(log n) or O(1) required
```
