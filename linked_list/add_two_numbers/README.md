# LeetCode 2 — Add Two Numbers

## Problem

Two linked lists represent non-negative integers.
Their digits are stored in reverse order.
Add the numbers and return the result as a linked list,
also in reverse order.

## Example

- First list: 2 → 4 → 3 represents 342.
- Second list: 5 → 6 → 4 represents 465.
- Sum: 342 + 465 = 807.
- Result: 7 → 0 → 8.

## Approach

Add corresponding digits while tracking a carry.

1. Create a dummy node to simplify building the result.
2. Start with carry = 0.
3. Add the current digits and the carry.
4. Use total % 10 to get the result digit.
5. Use total // 10 to get the new carry.
6. Append a new node containing the result digit.
7. Continue while either list has nodes or a carry remains.
8. Return dummy.next to skip the placeholder node.

A missing digit in a shorter list contributes zero.

## Dry Run

| First digit | Second digit | Carry in | Total | Result digit | Carry out |
|---|---|---|---|---|---|
| 2 | 5 | 0 | 7 | 7 | 0 |
| 4 | 6 | 0 | 10 | 0 | 1 |
| 3 | 4 | 1 | 8 | 8 | 0 |

Result: 7 → 0 → 8.

## Complexity

For lists of lengths m and n:

- Time: O(max(m, n)).
- Extra space excluding the output: O(1).
- Output space: O(max(m, n)).

## Solution

See [solution.py](solution.py).

ListNode is provided by the LeetCode environment.
