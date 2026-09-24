cat > README.md << 'EOF'
# 21. Merge Two Sorted Lists

**Difficulty:** Easy
**Topic:** Linked List / Two Pointers

---

## Problem Description

You are given the heads of two sorted linked lists `list1` and `list2`.

Merge the two lists into one sorted list. The list should be made by splicing together the nodes of the first two lists.

Return the head of the merged linked list.

### Example

Input: list1 = [1,2,4], list2 = [1,3,4]
Output: [1,1,2,3,4,4]

Input: list1 = [], list2 = []
Output: []

Input: list1 = [], list2 = [0]
Output: [0]

### Constraints

- The number of nodes in both lists is in the range [0, 50].
- -100 <= Node.val <= 100
- Both list1 and list2 are sorted in non-decreasing order.

---

## Approach

Use a **dummy head node** and a **tail pointer** to build the merged list by relinking existing nodes (no new nodes are created):

1. Create a dummy node as a placeholder before the real head.
2. Use tail to track the last node added to the merged list, starting at dummy.
3. Walk list1 and list2 together. At each step, compare the current nodes' values and attach the smaller one to tail.next, then advance that list's pointer and tail.
4. Once one list is exhausted, attach the remaining (already sorted) nodes from the other list directly.
5. Return dummy.next, the real head of the merged list.

## Complexity

- **Time:** O(n + m), where n and m are the lengths of list1 and list2.
- **Space:** O(1) extra space — nodes are relinked, not copied.

## Code

See [merge_two_sorted_lists.py](./merge_two_sorted_lists.py)
EOF
