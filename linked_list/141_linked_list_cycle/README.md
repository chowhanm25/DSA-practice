# 141. Linked List Cycle

**Difficulty:** Easy
**Topic:** Linked List / Two Pointers

## Problem Description
Given the head of a linked list, return `True` if following `next` pointers can lead back to a node you already visited. Otherwise, return `False`.

## Approach
Start `slow` and `fast` at the head. Move `slow` one node and `fast` two nodes each iteration. If they meet, the list has a cycle. If `fast` reaches the end, the list has no cycle. The `pos` value used to describe test cases is not an input to the function.

## Complexity
- Time: O(n) — each iteration advances through the list
- Space: O(1) — only two pointers are used
