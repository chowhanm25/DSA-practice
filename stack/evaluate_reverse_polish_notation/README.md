# 150. Evaluate Reverse Polish Notation

## 📌 Problem Statement

You are given an array of strings `tokens` that represents an arithmetic expression in **Reverse Polish Notation (RPN)**.

Evaluate the expression and return the integer result.

### Valid Operators:
- `+`
- `-`
- `*`
- `/`

### Notes:
- Division between two integers truncates toward zero.
- No division by zero.
- Input is always valid.
- Intermediate and final results fit in a 32-bit integer.

---

## 🧠 Approach

We use a **Stack (LIFO)** data structure.

### Algorithm:
1. Initialize an empty stack.
2. Traverse each token:
   - If the token is a number → push it onto the stack.
   - If the token is an operator:
     - Pop two elements from the stack.
     - Apply the operator.
     - Push the result back onto the stack.
3. The final answer will be the only element left in the stack.

---

## 💡 Key Insight

Reverse Polish Notation evaluates expressions **without parentheses**  
because operator order is determined by position.

Example:

Input:
