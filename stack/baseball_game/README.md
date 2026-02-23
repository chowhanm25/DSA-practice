# Baseball Game (LeetCode 682)

## Problem
You are keeping track of a baseball game with the following rules:

- Integer x: Record x points.
- "+": Record points equal to the sum of the previous two scores.
- "D": Record points equal to double the previous score.
- "C": Invalidate the previous score.

Return the total points after all operations.

### Example

Input: ["5","2","C","D","+"]  
Output: 30  

Step-by-step:

1. "5" → [5]  
2. "2" → [5, 2]  
3. "C" → [5]  
4. "D" → [5, 10]  
5. "+" → [5, 10, 15]  
Sum = 30

---

## Approach: Stack

We use a stack to store the valid scores.

Rules:

- "C" → `pop()` last element  
- "D" → `append(2 * stack[-1])`  
- "+" → `append(stack[-1] + stack[-2])`  
- Number → `append(int(num))`  

---

## Complexity

- Time: O(n)  
- Space: O(n)  

Each operation is done once.

---

## Key Concept

Stack is perfect because each operation depends on **previous elements only**.
