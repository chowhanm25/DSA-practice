# 304. Range Sum Query 2D – Immutable

This solution implements the **NumMatrix** class using a **2D Prefix Sum** technique to efficiently answer submatrix sum queries.

---

## Approach

A prefix sum matrix is constructed such that each cell stores the cumulative sum of elements from the origin to that cell.  
This enables constant-time region sum queries.

---

## Complexity Analysis

- **Preprocessing Time:** O(m × n)
- **Query Time:** O(1)
- **Space Complexity:** O(m × n)

---

## Key Concepts

- Prefix Sum
- Matrix Preprocessing
- Efficient Query Optimization

---

## Language

- Python

