# Data Structures & Algorithms Interview Guide

## Overview

This guide covers the core data structures and algorithms topics you'll encounter in technical interviews. It's structured to help you build a mental model for each topic, recognize patterns, and apply systematic frameworks when answering questions under pressure.

**Topics covered:** Arrays, Linked Lists, Trees, Graphs, Hash Maps, Sorting, Searching

---

## Key Concepts

### Arrays
- Contiguous block of memory; O(1) random access by index
- Insertion/deletion at arbitrary positions is O(n) due to shifting
- Common patterns: two pointers, sliding window, prefix sums, kadane's algorithm
- Know: dynamic arrays (amortized O(1) append), multi-dimensional arrays

### Linked Lists
- Nodes with data + pointer(s) to next (and previous for doubly linked)
- O(1) insert/delete at known position; O(n) search
- Common patterns: fast/slow pointers (Floyd's cycle detection), reversal, merge
- Know: singly vs doubly linked, sentinel/dummy nodes, in-place reversal

### Trees
- Hierarchical structure; root, parent, child, leaf nodes
- Binary Tree: each node has at most 2 children
- Binary Search Tree (BST): left < root < right; O(log n) average for search/insert/delete
- Balanced BSTs (AVL, Red-Black): guarantee O(log n) worst case
- Common patterns: DFS (pre/in/post-order), BFS (level-order), recursion, path problems
- Know: height vs depth, complete vs full vs perfect binary trees, tree serialization

### Graphs
- Nodes (vertices) connected by edges; can be directed or undirected, weighted or unweighted
- Representations: adjacency list (sparse graphs), adjacency matrix (dense graphs)
- Common patterns: BFS (shortest path in unweighted), DFS (cycle detection, topological sort), Dijkstra (weighted shortest path), Union-Find (connected components)
- Know: DAGs, topological sort, strongly connected components, bipartite graphs

### Hash Maps
- Key-value store with O(1) average insert, delete, lookup
- Collisions handled via chaining or open addressing
- Common patterns: frequency counting, two-sum style lookups, grouping/bucketing, memoization
- Know: load factor, hash functions, when worst case O(n) occurs

### Sorting
- Comparison-based lower bound: O(n log n)
- In-place vs stable vs adaptive trade-offs matter for interview discussions
- Know: Bubble O(n²), Selection O(n²), Insertion O(n²) best O(n), Merge O(n log n) stable, Quick O(n log n) avg, Heap O(n log n), Counting/Radix O(n+k) non-comparison

### Searching
- Linear search O(n), Binary search O(log n) on sorted data
- BFS for shortest path / level-order; DFS for exhaustive exploration
- Know: binary search variants (first/last occurrence, rotated array), BFS vs DFS trade-offs

---

## Example Questions

### Q1: Two Sum
**Framework:** Hash Map — trade space for time to achieve O(n)

**Answer:**
> Iterate through the array. For each element `x`, check if `target - x` exists in a hash map. If yes, return the pair. If no, store `x` in the map.

```python
def two_sum(nums, target):
    seen = {}
    for i, x in enumerate(nums):
        complement = target - x
        if complement in seen:
            return [seen[complement], i]
        seen[x] = i
```

**Time:** O(n) | **Space:** O(n)

---

### Q2: Reverse a Linked List
**Framework:** Iterative pointer manipulation — track `prev`, `curr`, `next`

**Answer:**
> Walk the list, reversing each `next` pointer as you go. Maintain three pointers to avoid losing references.

```python
def reverse_list(head):
    prev, curr = None, head
    while curr:
        nxt = curr.next
        curr.next = prev
        prev = curr
        curr = nxt
    return prev
```

**Time:** O(n) | **Space:** O(1)

---

### Q3: Valid Parentheses
**Framework:** Stack — push open brackets, pop and match on close brackets

**Answer:**
> Use a stack. Push every opening bracket. On a closing bracket, check if the top of the stack is the matching opener. If not, or if the stack is empty, return false. At the end, the stack must be empty.

```python
def is_valid(s):
    stack = []
    mapping = {')': '(', '}': '{', ']': '['}
    for ch in s:
        if ch in mapping:
            top = stack.pop() if stack else '#'
            if mapping[ch] != top:
                return False
        else:
            stack.append(ch)
    return not stack
```

**Time:** O(n) | **Space:** O(n)

---

### Q4: Binary Tree Level Order Traversal
**Framework:** BFS with a queue — process nodes level by level

**Answer:**
> Use a queue initialized with the root. At each level, record the queue size, process exactly that many nodes, and enqueue their children. Collect results per level.

```python
from collections import deque

def level_order(root):
    if not root:
        return []
    result, queue = [], deque([root])
    while queue:
        level = []
        for _ in range(len(queue)):
            node = queue.popleft()
            level.append(node.val)
            if node.left: queue.append(node.left)
            if node.right: queue.append(node.right)
        result.append(level)
    return result
```

**Time:** O(n) | **Space:** O(n)

---

### Q5: Detect Cycle in a Linked List
**Framework:** Floyd's Cycle Detection — fast/slow pointers

**Answer:**
> Use two pointers: `slow` moves one step, `fast` moves two steps. If they ever meet, there's a cycle. If `fast` reaches null, there's no cycle.

```python
def has_cycle(head):
    slow, fast = head, head
    while fast and fast.next:
        slow = slow.next
        fast = fast.next.next
        if slow == fast:
            return True
    return False
```

**Time:** O(n) | **Space:** O(1)

---

### Q6: Number of Islands (Graph DFS/BFS)
**Framework:** Graph traversal — DFS/BFS to mark connected components

**Answer:**
> Iterate over every cell. When you find a `'1'` (land), increment the island count and run DFS/BFS to mark all connected land cells as visited (set to `'0'`).

```python
def num_islands(grid):
    if not grid:
        return 0
    count = 0
    def dfs(r, c):
        if r < 0 or r >= len(grid) or c < 0 or c >= len(grid[0]) or grid[r][c] != '1':
            return
        grid[r][c] = '0'
        for dr, dc in [(1,0),(-1,0),(0,1),(0,-1)]:
            dfs(r+dr, c+dc)
    for r in range(len(grid)):
        for c in range(len(grid[0])):
            if grid[r][c] == '1':
                dfs(r, c)
                count += 1
    return count
```

**Time:** O(m×n) | **Space:** O(m×n) recursion stack

---

### Q7: Merge Two Sorted Arrays
**Framework:** Two pointers — merge from the end to avoid extra space

**Answer:**
> Given `nums1` with extra space at the end and `nums2`, use three pointers starting from the back of each array and the merged result. Place the larger element at the current tail position.

```python
def merge(nums1, m, nums2, n):
    p1, p2, p = m - 1, n - 1, m + n - 1
    while p1 >= 0 and p2 >= 0:
        if nums1[p1] > nums2[p2]:
            nums1[p] = nums1[p1]; p1 -= 1
        else:
            nums1[p] = nums2[p2]; p2 -= 1
        p -= 1
    nums1[:p2+1] = nums2[:p2+1]
```

**Time:** O(m+n) | **Space:** O(1)

---

### Q8: Lowest Common Ancestor of a BST
**Framework:** BST property — navigate left/right based on value comparisons

**Answer:**
> In a BST, if both `p` and `q` are less than the current node, go left. If both are greater, go right. Otherwise, the current node is the LCA.

```python
def lowest_common_ancestor(root, p, q):
    while root:
        if p.val < root.val and q.val < root.val:
            root = root.left
        elif p.val > root.val and q.val > root.val:
            root = root.right
        else:
            return root
```

**Time:** O(log n) for balanced BST | **Space:** O(1)

---

### Q9: Find the Kth Largest Element
**Framework:** Min-heap of size k — maintain the k largest elements seen so far

**Answer:**
> Use a min-heap of size `k`. Push each element; if the heap exceeds size `k`, pop the smallest. The heap's root is the kth largest.

```python
import heapq

def find_kth_largest(nums, k):
    heap = []
    for num in nums:
        heapq.heappush(heap, num)
        if len(heap) > k:
            heapq.heappop(heap)
    return heap[0]
```

**Time:** O(n log k) | **Space:** O(k)

---

### Q10: Longest Substring Without Repeating Characters
**Framework:** Sliding window with a hash map — expand right, shrink left on duplicates

**Answer:**
> Maintain a window `[left, right]` and a map of character → last seen index. When a duplicate is found inside the window, move `left` past the previous occurrence. Track the maximum window size.

```python
def length_of_longest_substring(s):
    char_index = {}
    left = max_len = 0
    for right, ch in enumerate(s):
        if ch in char_index and char_index[ch] >= left:
            left = char_index[ch] + 1
        char_index[ch] = right
        max_len = max(max_len, right - left + 1)
    return max_len
```

**Time:** O(n) | **Space:** O(min(n, alphabet_size))

---

### Q11: Binary Search
**Framework:** Divide and conquer — eliminate half the search space each iteration

**Answer:**
> Maintain `lo` and `hi` pointers. Compute `mid = lo + (hi - lo) // 2` (avoids overflow). If `nums[mid] == target`, return `mid`. If `target < nums[mid]`, search left half; otherwise search right half.

```python
def binary_search(nums, target):
    lo, hi = 0, len(nums) - 1
    while lo <= hi:
        mid = lo + (hi - lo) // 2
        if nums[mid] == target:
            return mid
        elif nums[mid] < target:
            lo = mid + 1
        else:
            hi = mid - 1
    return -1
```

**Time:** O(log n) | **Space:** O(1)

---

### Q12: Course Schedule (Topological Sort / Cycle Detection)
**Framework:** DFS with coloring — detect back edges in a directed graph

**Answer:**
> Model courses as a directed graph. Use DFS with three states: unvisited (0), visiting (1), visited (2). If you reach a node in state "visiting", there's a cycle and the schedule is impossible.

```python
def can_finish(num_courses, prerequisites):
    graph = [[] for _ in range(num_courses)]
    for a, b in prerequisites:
        graph[b].append(a)
    state = [0] * num_courses

    def dfs(node):
        if state[node] == 1: return False  # cycle
        if state[node] == 2: return True   # already processed
        state[node] = 1
        for neighbor in graph[node]:
            if not dfs(neighbor): return False
        state[node] = 2
        return True

    return all(dfs(i) for i in range(num_courses))
```

**Time:** O(V+E) | **Space:** O(V+E)

---

## Practice Resources

### Recommended Platforms
- [LeetCode](https://leetcode.com) — industry standard; filter by topic and difficulty
- [NeetCode](https://neetcode.io) — curated 150-problem list with video explanations
- [HackerRank](https://hackerrank.com) — good for structured tracks
- [AlgoExpert](https://algoexpert.io) — video walkthroughs for common interview problems

### Study Order (Recommended)
1. Arrays & Hashing
2. Two Pointers & Sliding Window
3. Stack & Queue
4. Binary Search
5. Linked Lists
6. Trees (DFS/BFS)
7. Heap / Priority Queue
8. Graphs (BFS/DFS, Union-Find)
9. Dynamic Programming
10. Advanced (Tries, Segment Trees, etc.)

### Key Patterns to Master
| Pattern | When to Use |
|---|---|
| Two Pointers | Sorted arrays, palindromes, pair sums |
| Sliding Window | Subarray/substring with constraint |
| Fast/Slow Pointers | Cycle detection, middle of list |
| BFS | Shortest path, level-order traversal |
| DFS | Exhaustive search, tree traversal, backtracking |
| Hash Map | O(1) lookup, frequency counting, grouping |
| Binary Search | Sorted data, search space reduction |
| Heap | Top-k elements, streaming median |
| Dynamic Programming | Overlapping subproblems, optimal substructure |

### Additional Reading
- *Cracking the Coding Interview* — Gayle Laakmann McDowell
- *Introduction to Algorithms (CLRS)* — for deep theoretical grounding
- [Big-O Cheatsheet](./Big-O-Cheatsheet.md) — quick complexity reference
- [Practice Problems](./Practice-Problems.md) — 30+ curated problems by topic
