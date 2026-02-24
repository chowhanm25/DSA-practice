# Stack Using Queues

## Problem
Implement a last-in-first-out (LIFO) stack using only two queues. The stack should support the following operations:
- `push(x)`: Push element x to the top of the stack.
- `pop()`: Removes the element on the top of the stack and returns it.
- `top()`: Returns the element on the top of the stack.
- `empty()`: Returns true if the stack is empty, false otherwise.

## Approach

### 1. Single Queue (Costly Push)
- Push: O(n)
- Pop: O(1)
- Top: O(1)
- Idea: Rotate the queue after every push so the new element becomes the front.

### 2. Two Queues (Costly Pop)
- Push: O(1)
- Pop: O(n)
- Top: O(n)
- Idea: Use a second queue to temporarily hold all elements except the last during pop/top operations.
