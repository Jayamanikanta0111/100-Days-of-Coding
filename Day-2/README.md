# Day 2: Sorting Algorithms – Merge Sort and Quick Sort

This repository contains Python implementations of two fundamental sorting algorithms:

- **Merge Sort**
- **Quick Sort**

These are classic examples of divide-and-conquer algorithms, each with its own use cases and performance characteristics.

---

## 📁 Files

- `Merge_sort.py`: Implements the Merge Sort algorithm.
- `Quick_sort.py`: Implements the Quick Sort algorithm.

---

## 🧠 Algorithms Overview

### 🧩 Merge Sort

- **Approach**: Divide-and-conquer
- **Time Complexity**: O(n log n)
- **Space Complexity**: O(n)
- **Stable**: Yes

#### How it works:
1. Recursively splits the list into halves until base case is reached.
2. Merges sorted halves using the `Merge` function.


## ⚡ Quick Sort

**Time Complexity**: O(n log n) average, O(n²) worst case  
**Space Complexity**: O(log n)  
**Stable**: ❌ No

### Description

Quick Sort selects a **pivot element**, partitions the array around the pivot, and recursively applies the same process to subarrays.

It’s generally faster than Merge Sort for small or in-place arrays, though it has a worst-case time of O(n²) if the pivot is poorly chosen.

#### How it works:
1. Selects a pivot element (typically the last element in the current subarray).
2. Partitions the array so that:
   - Elements less than or equal to the pivot go to the left.
   - Elements greater than the pivot go to the right.
3. Recursively applies the same process to the left and right subarrays.

## Summary

| Algorithm  | Time Complexity | Space Complexity | Stable | Best Use Case                |
| ---------- | --------------- | ---------------- | ------ | ---------------------------- |
| Merge Sort | O(n log n)      | O(n)             | Yes    | When stability is important  |
| Quick Sort | O(n log n)      | O(log n)         | No     | When in-place sort is needed |


