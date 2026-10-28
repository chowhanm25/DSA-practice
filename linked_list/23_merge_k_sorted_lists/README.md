# 23. Merge k Sorted Lists

- Difficulty: Hard
- Language: Python
- Problem: [Merge k Sorted Lists](https://leetcode.com/problems/merge-k-sorted-lists/)

## Approach

Use divide and conquer to merge the linked lists in pairs:

- Merge two sorted linked lists by repeatedly attaching the smaller node.
- Once one list ends, attach the remaining nodes from the other list.
- Store each merged list's head for the next round.
- Repeat until only one linked list remains.

If a round has an unpaired list, carry it forward by merging it with None.
The solution reuses existing nodes.

## Complexity

Let N be the total number of nodes and k the number of input lists.

- Time: O(k + N log(k + 1)), commonly described as O(N log k).
- Extra space: O(k) for the temporary lists of heads.
- Each two-list merge uses O(1) extra space.

## Solution

See [solution.py](solution.py). LeetCode provides the ListNode class.
