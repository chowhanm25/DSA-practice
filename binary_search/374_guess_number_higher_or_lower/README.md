# 374. Guess Number Higher or Lower

## Problem

We are playing a game where a number is picked from `1` to `n`.
You have to guess the number using the provided API:

* `-1` → your guess is too high
* `1` → your guess is too low
* `0` → correct guess

Return the number that was picked.

## Approach

We use **Binary Search** on the range `[1, n]`.

1. Start with `left = 1` and `right = n`
2. Find `mid`
3. Call `guess(mid)`:

   * If `0` → return `mid`
   * If `-1` → search left half
   * If `1` → search right half
4. Repeat until the number is found

## Complexity

* **Time Complexity:** O(log n)
* **Space Complexity:** O(1)

