# Sorting Algorithms

A reference for four fundamental sorting algorithms. Each entry includes a plain-English explanation, pseudocode, Python implementation, and Big-O complexity analysis.

## Table of Contents

- [Bubble Sort](#bubble-sort)
- [Merge Sort](#merge-sort)
- [Quick Sort](#quick-sort)
- [Heap Sort](#heap-sort)

---

## Bubble Sort

**Category:** Sorting
**Time Complexity:** O(n²) average and worst case; O(n) best case (already sorted)
**Space Complexity:** O(1)

### Explanation

Bubble Sort repeatedly steps through the list, compares adjacent elements, and swaps them if they are in the wrong order. Each full pass "bubbles" the largest unsorted element to its correct position at the end. The process repeats until no swaps are needed, meaning the list is sorted.

It is one of the simplest sorting algorithms to understand but is inefficient on large lists. It is mainly useful for educational purposes or for nearly-sorted data where the O(n) best case applies.

### Pseudocode

```text
procedure bubbleSort(arr):
    n = length of arr
    repeat
        swapped = false
        for i from 0 to n - 2:
            if arr[i] > arr[i + 1]:
                swap arr[i] and arr[i + 1]
                swapped = true
        n = n - 1
    until swapped is false
    return arr
```

### Implementation

```python
def bubble_sort(arr):
    n = len(arr)
    for i in range(n):
        swapped = False
        # Last i elements are already in place
        for j in range(0, n - i - 1):
            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]
                swapped = True
        # If no swap occurred, the array is already sorted
        if not swapped:
            break
    return arr


# Example usage
if __name__ == "__main__":
    data = [64, 34, 25, 12, 22, 11, 90]
    print("Sorted:", bubble_sort(data))
    # Output: Sorted: [11, 12, 22, 25, 34, 64, 90]
```

---

## Merge Sort

**Category:** Sorting
**Time Complexity:** O(n log n) — all cases
**Space Complexity:** O(n)

### Explanation

Merge Sort is a divide-and-conquer algorithm. It recursively splits the array in half until each sub-array contains a single element (which is trivially sorted), then merges those sub-arrays back together in sorted order.

The merge step compares the front elements of two sorted halves and picks the smaller one, building a sorted result. Because it always splits evenly and merges linearly, it guarantees O(n log n) in all cases. The trade-off is O(n) extra space for the temporary arrays used during merging.

Merge Sort is stable (preserves the relative order of equal elements) and is the algorithm of choice when stability matters or when sorting linked lists.

### Pseudocode

```text
procedure mergeSort(arr):
    if length of arr <= 1:
        return arr

    mid = length of arr / 2
    left = mergeSort(arr[0..mid])
    right = mergeSort(arr[mid..end])

    return merge(left, right)

procedure merge(left, right):
    result = []
    while left is not empty and right is not empty:
        if left[0] <= right[0]:
            append left[0] to result
            remove left[0] from left
        else:
            append right[0] to result
            remove right[0] from right
    append remaining elements of left to result
    append remaining elements of right to result
    return result
```

### Implementation

```python
def merge_sort(arr):
    if len(arr) <= 1:
        return arr

    mid = len(arr) // 2
    left = merge_sort(arr[:mid])
    right = merge_sort(arr[mid:])

    return merge(left, right)


def merge(left, right):
    result = []
    i = j = 0

    while i < len(left) and j < len(right):
        if left[i] <= right[j]:
            result.append(left[i])
            i += 1
        else:
            result.append(right[j])
            j += 1

    # Append any remaining elements
    result.extend(left[i:])
    result.extend(right[j:])
    return result


# Example usage
if __name__ == "__main__":
    data = [38, 27, 43, 3, 9, 82, 10]
    print("Sorted:", merge_sort(data))
    # Output: Sorted: [3, 9, 10, 27, 38, 43, 82]
```

---

## Quick Sort

**Category:** Sorting
**Time Complexity:** O(n log n) average; O(n²) worst case (poor pivot selection)
**Space Complexity:** O(log n) average (call stack)

### Explanation

Quick Sort is a divide-and-conquer algorithm that selects a "pivot" element and partitions the array into two sub-arrays: elements less than the pivot and elements greater than the pivot. It then recursively sorts each sub-array.

The key insight is the partition step — it rearranges elements in-place so that everything to the left of the pivot is smaller and everything to the right is larger. After partitioning, the pivot is in its final sorted position.

Quick Sort is typically faster in practice than Merge Sort due to better cache performance and lower constant factors, even though both are O(n log n) on average. The worst case O(n²) occurs when the pivot is always the smallest or largest element (e.g., already-sorted input with a naive pivot choice). Randomizing the pivot selection mitigates this.

### Pseudocode

```text
procedure quickSort(arr, low, high):
    if low < high:
        pivotIndex = partition(arr, low, high)
        quickSort(arr, low, pivotIndex - 1)
        quickSort(arr, pivotIndex + 1, high)

procedure partition(arr, low, high):
    pivot = arr[high]
    i = low - 1
    for j from low to high - 1:
        if arr[j] <= pivot:
            i = i + 1
            swap arr[i] and arr[j]
    swap arr[i + 1] and arr[high]
    return i + 1
```

### Implementation

```python
def quick_sort(arr, low=0, high=None):
    if high is None:
        high = len(arr) - 1

    if low < high:
        pivot_index = partition(arr, low, high)
        quick_sort(arr, low, pivot_index - 1)
        quick_sort(arr, pivot_index + 1, high)

    return arr


def partition(arr, low, high):
    pivot = arr[high]
    i = low - 1  # Index of smaller element

    for j in range(low, high):
        if arr[j] <= pivot:
            i += 1
            arr[i], arr[j] = arr[j], arr[i]

    # Place pivot in correct position
    arr[i + 1], arr[high] = arr[high], arr[i + 1]
    return i + 1


# Example usage
if __name__ == "__main__":
    data = [10, 7, 8, 9, 1, 5]
    print("Sorted:", quick_sort(data))
    # Output: Sorted: [1, 5, 7, 8, 9, 10]
```

---

## Heap Sort

**Category:** Sorting
**Time Complexity:** O(n log n) — all cases
**Space Complexity:** O(1)

### Explanation

Heap Sort uses a binary heap data structure to sort elements. It works in two phases:

1. **Build a max-heap** — Rearrange the array so that the largest element is at the root (index 0). This takes O(n) time.
2. **Extract elements** — Repeatedly swap the root (maximum) with the last element of the heap, reduce the heap size by one, and restore the heap property (heapify). Each extraction takes O(log n), and doing this n times gives O(n log n) total.

Heap Sort is in-place (O(1) space) and guarantees O(n log n) in all cases, unlike Quick Sort. However, it is not stable and tends to have worse cache performance than Merge Sort or Quick Sort in practice.

### Pseudocode

```text
procedure heapSort(arr):
    n = length of arr

    // Build max-heap
    for i from n/2 - 1 down to 0:
        heapify(arr, n, i)

    // Extract elements from heap one by one
    for i from n - 1 down to 1:
        swap arr[0] and arr[i]
        heapify(arr, i, 0)

procedure heapify(arr, n, i):
    largest = i
    left = 2 * i + 1
    right = 2 * i + 2

    if left < n and arr[left] > arr[largest]:
        largest = left
    if right < n and arr[right] > arr[largest]:
        largest = right

    if largest != i:
        swap arr[i] and arr[largest]
        heapify(arr, n, largest)
```

### Implementation

```python
def heap_sort(arr):
    n = len(arr)

    # Build a max-heap
    for i in range(n // 2 - 1, -1, -1):
        heapify(arr, n, i)

    # Extract elements one by one
    for i in range(n - 1, 0, -1):
        # Move current root (max) to end
        arr[0], arr[i] = arr[i], arr[0]
        # Restore heap property on the reduced heap
        heapify(arr, i, 0)

    return arr


def heapify(arr, n, i):
    largest = i       # Assume root is largest
    left = 2 * i + 1
    right = 2 * i + 2

    # Check if left child is larger than root
    if left < n and arr[left] > arr[largest]:
        largest = left

    # Check if right child is larger than current largest
    if right < n and arr[right] > arr[largest]:
        largest = right

    # If largest is not root, swap and continue heapifying
    if largest != i:
        arr[i], arr[largest] = arr[largest], arr[i]
        heapify(arr, n, largest)


# Example usage
if __name__ == "__main__":
    data = [12, 11, 13, 5, 6, 7]
    print("Sorted:", heap_sort(data))
    # Output: Sorted: [5, 6, 7, 11, 12, 13]
```

---

## Complexity Summary

| Algorithm    | Best Case  | Average Case | Worst Case | Space    | Stable |
|--------------|------------|--------------|------------|----------|--------|
| Bubble Sort  | O(n)       | O(n²)        | O(n²)      | O(1)     | Yes    |
| Merge Sort   | O(n log n) | O(n log n)   | O(n log n) | O(n)     | Yes    |
| Quick Sort   | O(n log n) | O(n log n)   | O(n²)      | O(log n) | No     |
| Heap Sort    | O(n log n) | O(n log n)   | O(n log n) | O(1)     | No     |
