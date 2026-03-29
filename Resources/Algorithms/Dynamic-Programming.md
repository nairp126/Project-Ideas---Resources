# Dynamic Programming

A reference for three classic dynamic programming problems. Each entry includes a plain-English explanation, pseudocode, Python implementation, and Big-O complexity analysis.

## Table of Contents

- [What is Dynamic Programming?](#what-is-dynamic-programming)
- [Fibonacci Sequence](#fibonacci-sequence)
- [0/1 Knapsack](#01-knapsack)
- [Longest Common Subsequence (LCS)](#longest-common-subsequence-lcs)

---

## What is Dynamic Programming?

Dynamic Programming (DP) is an optimization technique for problems that have two key properties:

1. **Overlapping subproblems** — The problem can be broken into smaller subproblems that are solved multiple times.
2. **Optimal substructure** — The optimal solution to the problem can be built from optimal solutions to its subproblems.

DP avoids redundant computation by storing results of subproblems. There are two main approaches:

- **Memoization (top-down)** — Solve recursively, cache results as you go.
- **Tabulation (bottom-up)** — Build a table of solutions from the smallest subproblems up.

---

## Fibonacci Sequence

**Category:** Dynamic Programming
**Time Complexity:** O(n) with memoization or tabulation; O(2ⁿ) naive recursive
**Space Complexity:** O(n) memoization/tabulation; O(1) space-optimized

### Explanation

The Fibonacci sequence is defined as: F(0) = 0, F(1) = 1, and F(n) = F(n-1) + F(n-2) for n > 1.

The naive recursive solution recalculates the same values many times — F(5) calls F(4) and F(3), F(4) calls F(3) and F(2), and so on. This leads to exponential time O(2ⁿ).

Dynamic programming solves this by storing each computed value so it is only calculated once:
- **Memoization**: Add a cache to the recursive solution. On each call, check the cache before computing.
- **Tabulation**: Build an array from F(0) up to F(n), using previously computed values.
- **Space-optimized**: Since F(n) only depends on the previous two values, you only need two variables.

### Pseudocode

```text
// Memoization (top-down)
procedure fib_memo(n, memo):
    if n in memo: return memo[n]
    if n <= 1: return n
    memo[n] = fib_memo(n - 1, memo) + fib_memo(n - 2, memo)
    return memo[n]

// Tabulation (bottom-up)
procedure fib_tab(n):
    if n <= 1: return n
    dp = array of size n + 1
    dp[0] = 0
    dp[1] = 1
    for i from 2 to n:
        dp[i] = dp[i - 1] + dp[i - 2]
    return dp[n]
```

### Implementation

```python
def fib_naive(n):
    """Naive recursive — O(2^n) time. Avoid for large n."""
    if n <= 1:
        return n
    return fib_naive(n - 1) + fib_naive(n - 2)


def fib_memoized(n, memo=None):
    """Top-down DP with memoization — O(n) time, O(n) space."""
    if memo is None:
        memo = {}
    if n in memo:
        return memo[n]
    if n <= 1:
        return n
    memo[n] = fib_memoized(n - 1, memo) + fib_memoized(n - 2, memo)
    return memo[n]


def fib_tabulated(n):
    """Bottom-up DP with tabulation — O(n) time, O(n) space."""
    if n <= 1:
        return n
    dp = [0] * (n + 1)
    dp[1] = 1
    for i in range(2, n + 1):
        dp[i] = dp[i - 1] + dp[i - 2]
    return dp[n]


def fib_optimized(n):
    """Space-optimized DP — O(n) time, O(1) space."""
    if n <= 1:
        return n
    prev2, prev1 = 0, 1
    for _ in range(2, n + 1):
        current = prev1 + prev2
        prev2, prev1 = prev1, current
    return prev1


# Example usage
if __name__ == "__main__":
    n = 10
    print(f"fib({n}) naive:     {fib_naive(n)}")
    print(f"fib({n}) memoized:  {fib_memoized(n)}")
    print(f"fib({n}) tabulated: {fib_tabulated(n)}")
    print(f"fib({n}) optimized: {fib_optimized(n)}")
    # All output: 55

    # First 10 Fibonacci numbers
    print("Sequence:", [fib_optimized(i) for i in range(10)])
    # Output: [0, 1, 1, 2, 3, 5, 8, 13, 21, 34]
```

---

## 0/1 Knapsack

**Category:** Dynamic Programming
**Time Complexity:** O(n × W) where n = number of items, W = knapsack capacity
**Space Complexity:** O(n × W); O(W) with space optimization

### Explanation

The 0/1 Knapsack problem: given a set of items, each with a weight and a value, determine which items to include in a knapsack of limited capacity to maximize the total value. Each item can either be included (1) or excluded (0) — you cannot take a fraction of an item.

The DP approach builds a 2D table `dp[i][w]` representing the maximum value achievable using the first `i` items with a knapsack capacity of `w`. For each item, you decide:
- **Skip it**: `dp[i][w] = dp[i-1][w]`
- **Take it** (if it fits): `dp[i][w] = dp[i-1][w - weight[i]] + value[i]`

You take the maximum of these two choices. After filling the table, `dp[n][W]` holds the answer.

### Pseudocode

```text
procedure knapsack(weights, values, capacity):
    n = number of items
    dp = 2D array of size (n + 1) x (capacity + 1), initialized to 0

    for i from 1 to n:
        for w from 0 to capacity:
            // Option 1: skip item i
            dp[i][w] = dp[i - 1][w]
            // Option 2: take item i (if it fits)
            if weights[i - 1] <= w:
                take_value = dp[i - 1][w - weights[i - 1]] + values[i - 1]
                dp[i][w] = max(dp[i][w], take_value)

    return dp[n][capacity]
```

### Implementation

```python
def knapsack(weights, values, capacity):
    """
    0/1 Knapsack using bottom-up DP.
    weights: list of item weights
    values:  list of item values (same length as weights)
    capacity: maximum weight the knapsack can hold
    Returns the maximum value achievable.
    """
    n = len(weights)
    # dp[i][w] = max value using first i items with capacity w
    dp = [[0] * (capacity + 1) for _ in range(n + 1)]

    for i in range(1, n + 1):
        for w in range(capacity + 1):
            # Option 1: skip item i
            dp[i][w] = dp[i - 1][w]
            # Option 2: take item i if it fits
            if weights[i - 1] <= w:
                take = dp[i - 1][w - weights[i - 1]] + values[i - 1]
                dp[i][w] = max(dp[i][w], take)

    return dp[n][capacity]


def knapsack_with_items(weights, values, capacity):
    """
    0/1 Knapsack that also returns which items were selected.
    Returns (max_value, list of selected item indices).
    """
    n = len(weights)
    dp = [[0] * (capacity + 1) for _ in range(n + 1)]

    for i in range(1, n + 1):
        for w in range(capacity + 1):
            dp[i][w] = dp[i - 1][w]
            if weights[i - 1] <= w:
                take = dp[i - 1][w - weights[i - 1]] + values[i - 1]
                dp[i][w] = max(dp[i][w], take)

    # Backtrack to find selected items
    selected = []
    w = capacity
    for i in range(n, 0, -1):
        if dp[i][w] != dp[i - 1][w]:
            selected.append(i - 1)  # Item index (0-based)
            w -= weights[i - 1]

    return dp[n][capacity], selected[::-1]


def knapsack_optimized(weights, values, capacity):
    """Space-optimized 0/1 Knapsack — O(W) space."""
    n = len(weights)
    dp = [0] * (capacity + 1)

    for i in range(n):
        # Traverse right-to-left to avoid using the same item twice
        for w in range(capacity, weights[i] - 1, -1):
            dp[w] = max(dp[w], dp[w - weights[i]] + values[i])

    return dp[capacity]


# Example usage
if __name__ == "__main__":
    weights = [2, 3, 4, 5]
    values  = [3, 4, 5, 6]
    capacity = 8

    max_val = knapsack(weights, values, capacity)
    print(f"Max value: {max_val}")
    # Output: Max value: 10

    max_val, items = knapsack_with_items(weights, values, capacity)
    print(f"Max value: {max_val}, Items selected (0-indexed): {items}")
    # Output: Max value: 10, Items selected (0-indexed): [1, 3]
    # Items at index 1 (weight=3, value=4) and index 3 (weight=5, value=6) → total weight=8, value=10
```

---

## Longest Common Subsequence (LCS)

**Category:** Dynamic Programming
**Time Complexity:** O(m × n) where m and n are the lengths of the two strings
**Space Complexity:** O(m × n); O(min(m, n)) with space optimization

### Explanation

The Longest Common Subsequence problem finds the longest sequence of characters that appears in the same relative order in both strings, but not necessarily contiguously.

For example, LCS("ABCBDAB", "BDCAB") = "BCAB" or "BDAB" (length 4).

The DP approach builds a 2D table `dp[i][j]` representing the length of the LCS of the first `i` characters of string 1 and the first `j` characters of string 2:
- If `s1[i-1] == s2[j-1]`: `dp[i][j] = dp[i-1][j-1] + 1` (extend the LCS)
- Otherwise: `dp[i][j] = max(dp[i-1][j], dp[i][j-1])` (take the best without one character)

LCS is foundational for diff tools, version control systems, and bioinformatics sequence alignment.

### Pseudocode

```text
procedure lcs(s1, s2):
    m = length of s1
    n = length of s2
    dp = 2D array of size (m + 1) x (n + 1), initialized to 0

    for i from 1 to m:
        for j from 1 to n:
            if s1[i - 1] == s2[j - 1]:
                dp[i][j] = dp[i - 1][j - 1] + 1
            else:
                dp[i][j] = max(dp[i - 1][j], dp[i][j - 1])

    return dp[m][n]
```

### Implementation

```python
def lcs_length(s1, s2):
    """
    Returns the length of the Longest Common Subsequence of s1 and s2.
    """
    m, n = len(s1), len(s2)
    dp = [[0] * (n + 1) for _ in range(m + 1)]

    for i in range(1, m + 1):
        for j in range(1, n + 1):
            if s1[i - 1] == s2[j - 1]:
                dp[i][j] = dp[i - 1][j - 1] + 1
            else:
                dp[i][j] = max(dp[i - 1][j], dp[i][j - 1])

    return dp[m][n]


def lcs_string(s1, s2):
    """
    Returns the actual LCS string (not just its length) by backtracking the DP table.
    """
    m, n = len(s1), len(s2)
    dp = [[0] * (n + 1) for _ in range(m + 1)]

    for i in range(1, m + 1):
        for j in range(1, n + 1):
            if s1[i - 1] == s2[j - 1]:
                dp[i][j] = dp[i - 1][j - 1] + 1
            else:
                dp[i][j] = max(dp[i - 1][j], dp[i][j - 1])

    # Backtrack to reconstruct the LCS
    lcs = []
    i, j = m, n
    while i > 0 and j > 0:
        if s1[i - 1] == s2[j - 1]:
            lcs.append(s1[i - 1])
            i -= 1
            j -= 1
        elif dp[i - 1][j] > dp[i][j - 1]:
            i -= 1
        else:
            j -= 1

    return ''.join(reversed(lcs))


def lcs_optimized(s1, s2):
    """Space-optimized LCS — O(min(m, n)) space, returns length only."""
    if len(s1) < len(s2):
        s1, s2 = s2, s1  # Ensure s2 is the shorter string

    m, n = len(s1), len(s2)
    prev = [0] * (n + 1)
    curr = [0] * (n + 1)

    for i in range(1, m + 1):
        for j in range(1, n + 1):
            if s1[i - 1] == s2[j - 1]:
                curr[j] = prev[j - 1] + 1
            else:
                curr[j] = max(prev[j], curr[j - 1])
        prev, curr = curr, [0] * (n + 1)

    return prev[n]


# Example usage
if __name__ == "__main__":
    s1 = "ABCBDAB"
    s2 = "BDCAB"

    print(f"LCS length: {lcs_length(s1, s2)}")
    # Output: LCS length: 4

    print(f"LCS string: {lcs_string(s1, s2)}")
    # Output: LCS string: BCAB  (one valid LCS)

    print(f"LCS optimized length: {lcs_optimized(s1, s2)}")
    # Output: LCS optimized length: 4

    # Another example
    s3, s4 = "AGGTAB", "GXTXAYB"
    print(f"\nLCS('{s3}', '{s4}') = '{lcs_string(s3, s4)}' (length {lcs_length(s3, s4)})")
    # Output: LCS('AGGTAB', 'GXTXAYB') = 'GTAB' (length 4)
```

---

## Complexity Summary

| Problem                    | Time Complexity | Space Complexity | Key Insight                              |
|----------------------------|-----------------|------------------|------------------------------------------|
| Fibonacci (naive)          | O(2ⁿ)           | O(n)             | Exponential — avoid for large n          |
| Fibonacci (DP)             | O(n)            | O(1) optimized   | Only need last two values                |
| 0/1 Knapsack               | O(n × W)        | O(W) optimized   | Include/exclude decision per item        |
| Longest Common Subsequence | O(m × n)        | O(min(m,n)) opt. | Match or skip characters from each string |
