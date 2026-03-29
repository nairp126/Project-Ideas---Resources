# Practice Problems

A curated list of 30+ coding problems organized by topic and difficulty. Use these alongside the [DSA Study Guide](./DSA-Study-Guide.md) and [Big-O Cheatsheet](./Big-O-Cheatsheet.md) to systematically prepare for technical interviews.

## Table of Contents

- [Arrays](#arrays)
- [Strings](#strings)
- [Linked Lists](#linked-lists)
- [Trees](#trees)
- [Graphs](#graphs)
- [Dynamic Programming](#dynamic-programming)
- [Sorting & Searching](#sorting--searching)
- [Hash Maps & Sets](#hash-maps--sets)
- [Study Tips](#study-tips)

---

## Arrays

| # | Problem | Difficulty | Notes |
|---|---------|------------|-------|
| 1 | [Two Sum](https://leetcode.com/problems/two-sum/) | 🟢 Easy | Classic hash map problem; great starting point |
| 2 | [Best Time to Buy and Sell Stock](https://leetcode.com/problems/best-time-to-buy-and-sell-stock/) | 🟢 Easy | Single-pass sliding window; track running minimum |
| 3 | [Contains Duplicate](https://leetcode.com/problems/contains-duplicate/) | 🟢 Easy | Hash set membership check |
| 4 | [Product of Array Except Self](https://leetcode.com/problems/product-of-array-except-self/) | 🟡 Medium | Prefix/suffix product trick; no division allowed |
| 5 | [Maximum Subarray](https://leetcode.com/problems/maximum-subarray/) | 🟡 Medium | Kadane's algorithm; classic DP on arrays |
| 6 | [3Sum](https://leetcode.com/problems/3sum/) | 🟡 Medium | Sort + two-pointer; watch for duplicate triplets |
| 7 | [Container With Most Water](https://leetcode.com/problems/container-with-most-water/) | 🟡 Medium | Two-pointer from both ends; greedy shrink |
| 8 | [Trapping Rain Water](https://leetcode.com/problems/trapping-rain-water/) | 🔴 Hard | Two-pointer or stack; visualize water levels |

---

## Strings

| # | Problem | Difficulty | Notes |
|---|---------|------------|-------|
| 9 | [Valid Anagram](https://leetcode.com/problems/valid-anagram/) | 🟢 Easy | Character frequency count; sort or hash map |
| 10 | [Valid Palindrome](https://leetcode.com/problems/valid-palindrome/) | 🟢 Easy | Two-pointer after filtering alphanumeric chars |
| 11 | [Longest Common Prefix](https://leetcode.com/problems/longest-common-prefix/) | 🟢 Easy | Vertical scan or sort and compare first/last |
| 12 | [Group Anagrams](https://leetcode.com/problems/group-anagrams/) | 🟡 Medium | Sort each string as key; hash map grouping |
| 13 | [Longest Substring Without Repeating Characters](https://leetcode.com/problems/longest-substring-without-repeating-characters/) | 🟡 Medium | Sliding window with a set; classic pattern |
| 14 | [Minimum Window Substring](https://leetcode.com/problems/minimum-window-substring/) | 🔴 Hard | Sliding window with two frequency maps |

---

## Linked Lists

| # | Problem | Difficulty | Notes |
|---|---------|------------|-------|
| 15 | [Reverse Linked List](https://leetcode.com/problems/reverse-linked-list/) | 🟢 Easy | Iterative (3 pointers) and recursive solutions |
| 16 | [Merge Two Sorted Lists](https://leetcode.com/problems/merge-two-sorted-lists/) | 🟢 Easy | Dummy head node simplifies edge cases |
| 17 | [Linked List Cycle](https://leetcode.com/problems/linked-list-cycle/) | 🟢 Easy | Floyd's slow/fast pointer (tortoise and hare) |
| 18 | [Remove Nth Node From End of List](https://leetcode.com/problems/remove-nth-node-from-end-of-list/) | 🟡 Medium | Two-pointer with N-gap; single pass |
| 19 | [Reorder List](https://leetcode.com/problems/reorder-list/) | 🟡 Medium | Find middle, reverse second half, merge |
| 20 | [Merge K Sorted Lists](https://leetcode.com/problems/merge-k-sorted-lists/) | 🔴 Hard | Min-heap or divide-and-conquer merge |

---

## Trees

| # | Problem | Difficulty | Notes |
|---|---------|------------|-------|
| 21 | [Maximum Depth of Binary Tree](https://leetcode.com/problems/maximum-depth-of-binary-tree/) | 🟢 Easy | DFS recursion or BFS level count |
| 22 | [Invert Binary Tree](https://leetcode.com/problems/invert-binary-tree/) | 🟢 Easy | Recursive swap; the famous Homebrew tweet problem |
| 23 | [Validate Binary Search Tree](https://leetcode.com/problems/validate-binary-search-tree/) | 🟡 Medium | Pass min/max bounds down recursion |
| 24 | [Lowest Common Ancestor of a BST](https://leetcode.com/problems/lowest-common-ancestor-of-a-binary-search-tree/) | 🟡 Medium | Use BST ordering to navigate left/right |
| 25 | [Binary Tree Level Order Traversal](https://leetcode.com/problems/binary-tree-level-order-traversal/) | 🟡 Medium | BFS with queue; track level boundaries |
| 26 | [Serialize and Deserialize Binary Tree](https://leetcode.com/problems/serialize-and-deserialize-binary-tree/) | 🔴 Hard | BFS or preorder with null markers |

---

## Graphs

| # | Problem | Difficulty | Notes |
|---|---------|------------|-------|
| 27 | [Number of Islands](https://leetcode.com/problems/number-of-islands/) | 🟡 Medium | DFS/BFS flood fill; mark visited in-place |
| 28 | [Clone Graph](https://leetcode.com/problems/clone-graph/) | 🟡 Medium | BFS/DFS with a visited hash map for clones |
| 29 | [Course Schedule](https://leetcode.com/problems/course-schedule/) | 🟡 Medium | Topological sort / cycle detection with DFS |
| 30 | [Pacific Atlantic Water Flow](https://leetcode.com/problems/pacific-atlantic-water-flow/) | 🟡 Medium | Reverse BFS from both oceans; find intersection |
| 31 | [Word Ladder](https://leetcode.com/problems/word-ladder/) | 🔴 Hard | BFS on implicit graph; wildcard pattern neighbors |

---

## Dynamic Programming

| # | Problem | Difficulty | Notes |
|---|---------|------------|-------|
| 32 | [Climbing Stairs](https://leetcode.com/problems/climbing-stairs/) | 🟢 Easy | Fibonacci pattern; great DP intro problem |
| 33 | [House Robber](https://leetcode.com/problems/house-robber/) | 🟡 Medium | 1D DP; rob[i] = max(rob[i-1], rob[i-2] + nums[i]) |
| 34 | [Coin Change](https://leetcode.com/problems/coin-change/) | 🟡 Medium | Bottom-up DP; unbounded knapsack variant |
| 35 | [Longest Increasing Subsequence](https://leetcode.com/problems/longest-increasing-subsequence/) | 🟡 Medium | O(n²) DP or O(n log n) with patience sorting |
| 36 | [Unique Paths](https://leetcode.com/problems/unique-paths/) | 🟡 Medium | 2D DP grid; combinatorics shortcut exists |
| 37 | [Edit Distance](https://leetcode.com/problems/edit-distance/) | 🔴 Hard | Classic 2D DP; Levenshtein distance |

---

## Sorting & Searching

| # | Problem | Difficulty | Notes |
|---|---------|------------|-------|
| 38 | [Binary Search](https://leetcode.com/problems/binary-search/) | 🟢 Easy | Template problem; nail the lo/hi/mid logic |
| 39 | [Search in Rotated Sorted Array](https://leetcode.com/problems/search-in-rotated-sorted-array/) | 🟡 Medium | Modified binary search; identify sorted half |
| 40 | [Find Minimum in Rotated Sorted Array](https://leetcode.com/problems/find-minimum-in-rotated-sorted-array/) | 🟡 Medium | Binary search on the pivot point |
| 41 | [Kth Largest Element in an Array](https://leetcode.com/problems/kth-largest-element-in-an-array/) | 🟡 Medium | Quickselect O(n) avg or min-heap O(n log k) |
| 42 | [Median of Two Sorted Arrays](https://leetcode.com/problems/median-of-two-sorted-arrays/) | 🔴 Hard | Binary search on partition; O(log(min(m,n))) |

---

## Hash Maps & Sets

| # | Problem | Difficulty | Notes |
|---|---------|------------|-------|
| 43 | [Ransom Note](https://leetcode.com/problems/ransom-note/) | 🟢 Easy | Character frequency comparison |
| 44 | [Top K Frequent Elements](https://leetcode.com/problems/top-k-frequent-elements/) | 🟡 Medium | Bucket sort or heap; O(n) bucket approach is elegant |
| 45 | [Longest Consecutive Sequence](https://leetcode.com/problems/longest-consecutive-sequence/) | 🟡 Medium | Hash set; only start counting from sequence beginnings |
| 46 | [LRU Cache](https://leetcode.com/problems/lru-cache/) | 🟡 Medium | Hash map + doubly linked list; O(1) get and put |

---

## Study Tips

**Recommended order for beginners:**
1. Start with Arrays and Strings (problems 1–14)
2. Move to Linked Lists and Trees (15–26)
3. Tackle Graphs and DP once comfortable with recursion (27–37)
4. Revisit Sorting & Searching and Hash Maps for interview polish (38–46)

**Difficulty legend:**
- 🟢 Easy — focus on correctness and clean code
- 🟡 Medium — the most common interview difficulty; aim to solve in 20–30 min
- 🔴 Hard — good for stretch goals; understand the approach even if you can't code it cold

**Practice strategy:**
- Solve each problem without hints first (set a 25-minute timer)
- Review the optimal solution even when you solve it — there's often a cleaner approach
- Re-solve problems you struggled with after 3–5 days (spaced repetition)
- For each problem, be able to explain the time and space complexity — see [Big-O Cheatsheet](./Big-O-Cheatsheet.md)
