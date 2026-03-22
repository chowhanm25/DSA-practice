# Koko Eating Bananas Problem

This is a solution to the "Koko Eating Bananas" problem.

## Problem

Koko loves to eat bananas. There are `n` piles of bananas, the ith pile has `piles[i]` bananas. Koko wants to eat all the bananas in `h` hours, and she can choose her eating speed `k` (bananas per hour). She eats from one pile per hour. If the pile has fewer than `k` bananas, she eats all of them.

**Goal:** Find the minimum integer `k` so that Koko can eat all the bananas within `h` hours.

## Solution

- Uses **binary search on answer** technique.
- Calculates total hours required for a given `k` using integer arithmetic: `(pile + k - 1) // k`.
- Time complexity: `O(n * log(max(piles)))`.
- Space complexity: `O(1)`.

## Example

```python
piles = [3,6,7,11]
h = 8
print(minEatingSpeed(piles, h))  # Output: 4
