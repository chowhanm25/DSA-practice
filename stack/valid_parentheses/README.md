
---

## Approach

We use a **Stack (LIFO)** data structure.

### Algorithm:

1. Create an empty stack.
2. Create a mapping of closing → opening brackets.
3. Traverse the string:
   - If opening bracket → push into stack.
   - If closing bracket:
     - Check if stack is empty → return False.
     - Check if top of stack matches → pop.
     - Otherwise → return False.
4. After traversal:
   - If stack is empty → valid.
   - Else → invalid.

---

## Complexity Analysis

- Time Complexity: **O(n)**
- Space Complexity: **O(n)**

---

## Key Concept

This problem is a classic **Stack pattern** where we validate matching pairs using LIFO behavior.
