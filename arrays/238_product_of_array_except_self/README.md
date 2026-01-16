# 238. Product of Array Except Self

This solution computes the product of all elements in the array except the current index, without using division and in linear time.

---

## Approach

The algorithm uses two passes:

1. **Left pass**  
   Stores the product of all elements to the left of each index.

2. **Right pass**  
   Multiplies each index by the product of all elements to the right.

The final result at each index is:
(left product) × (right product)

---

## Complexity Analysis

- **Time Complexity:** O(n)
- **Space Complexity:** O(1) extra space (excluding output array)

---

## Key Concepts

- Prefix Product
- Suffix Product
- Space Optimization
- Array Traversal

---

## Language

- Python

