# Maximum Frequency Stack

LeetCode Problem: 895  
Difficulty: Hard  
Topic: Stack, HashMap

## Problem

Design a stack-like data structure to push elements to the stack and pop the most frequent element from the stack.

Implement the `FreqStack` class:

- `FreqStack()` constructs an empty frequency stack.
- `void push(int val)` pushes an integer `val` onto the top of the stack.
- `int pop()` removes and returns the most frequent element in the stack.

If there is a tie for the most frequent element, the element closest to the stack's top is removed and returned.

---

## Example

Input

```
push(5)
push(7)
push(5)
push(7)
push(4)
push(5)
pop()
pop()
pop()
pop()
```

Output

```
5
7
5
4
```

---

## Approach

To solve this efficiently we maintain three structures:

### 1. Frequency Map

Tracks how many times each value appears.

```
freq[val] = frequency of val
```

Example

```
5 -> 3
7 -> 2
4 -> 1
```

---

### 2. Frequency → Stack Map

Each frequency has its own stack.

```
group[f] = stack of values with frequency f
```

Example

```
1 → [5,7,4]
2 → [5,7]
3 → [5]
```

This preserves the **order of insertion**, which helps resolve ties.

---

### 3. maxFreq

Tracks the **current highest frequency** in the stack.

```
maxFreq = 3
```

This allows us to immediately know where to pop from.

---

## Push Operation

Steps:

1. Increase the frequency of the value
2. Update `maxFreq`
3. Push the value into the stack corresponding to its frequency

---

## Pop Operation

Steps:

1. Pop from the stack with `maxFreq`
2. Decrease its frequency
3. If that stack becomes empty, decrease `maxFreq`

---

## Complexity

Time Complexity

```
push() → O(1)
pop()  → O(1)
```

Space Complexity

```
O(n)
```

---

## Key Idea

Instead of searching for the most frequent element each time, we organize elements **by their frequency** using stacks.  
This allows us to pop the **most frequent and most recent element in constant time**.
