# 69. Sqrt(x)

## Problem

Given a non-negative integer `x`, return the square root of `x` rounded down to the nearest integer.

You cannot use built-in functions like `pow()` or `x ** 0.5`.

## Approach

We use **Binary Search** to find the square root.

1. Search in range `1` to `x // 2`
2. Find `mid`
3. Check:

   * If `mid * mid == x` → return `mid`
   * If `mid * mid < x` → move right and store answer
   * If `mid * mid > x` → move left
4. Return the stored answer

## Complexity

* **Time Complexity:** O(log x)
* **Space Complexity:** O(1)

