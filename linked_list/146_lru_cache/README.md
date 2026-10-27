# 146. LRU Cache

- Difficulty: Medium
- Language: Python
- Problem: https://leetcode.com/problems/lru-cache/

## Approach

Use a dictionary and a doubly linked list:

- The dictionary maps each key to its node for fast lookup.
- The first real node is the least recently used.
- The last real node is the most recently used.
- Accessing or updating a key moves its node to the most recent position.
- When capacity is exceeded, remove the least recently used node from
  both the list and the dictionary.

Dummy nodes at both ends simplify insertion and removal.

## Complexity

- get: O(1) average time
- put: O(1) average time
- Space: O(capacity)

## Solution

See [solution.py](solution.py).
