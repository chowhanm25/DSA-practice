# 19. Remove Nth Node From End of List

- Difficulty: Medium
- Language: Python
- Approach: Two pointers and a dummy node
- [LeetCode problem](https://leetcode.com/problems/remove-nth-node-from-end-of-list/)

## Problem

Remove the nth node from the end of a singly linked list and return
the updated head.

## Examples

| Input list | n | Output list |
| --- | --- | --- |
| [1,2,3,4,5] | 2 | [1,2,3,5] |
| [1] | 1 | [] |
| [1,2] | 1 | [1] |

## Approach

1. Place a dummy node before the head.
2. Start fast and slow at the dummy node.
3. Move fast forward n times.
4. Move both pointers together until fast reaches the last node.
5. Slow now points to the node before the node to remove.
6. Remove the node using slow.next = slow.next.next.
7. Return dummy.next.

The dummy node also makes removing the first node straightforward.

## Complexity

Let L be the number of nodes.

- Time: O(L)
- Extra space: O(1)

## Solution

See [solution.py](solution.py).
