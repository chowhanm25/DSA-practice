# 206. Reverse Linked List

**Difficulty:** Easy
**Topic:** Linked List

## Problem Description
Given the head of a singly linked list, reverse the list, and return 
the reversed list's head.

## Approach
Iteratively walk through the list while reversing each node's `next` 
pointer to point backward instead of forward. Track three pointers: 
`prev` (the reversed portion built so far), `current` (the node being 
processed), and `next_node` (saved before overwriting, so the rest of 
the list isn't lost).

## Complexity
- Time: O(n) — single pass through the list
- Space: O(1) — only a few pointers used, no extra data structures