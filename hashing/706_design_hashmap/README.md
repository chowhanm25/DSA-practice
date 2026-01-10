# LeetCode 706: Design HashMap

**Difficulty:** Easy  
**Topic:** Hashing, Data Structure Design  

## Approach
- Implemented **Separate Chaining** (Array of Buckets) to handle collisions.
- Each bucket stores `[key, value]` pairs.
- `put` updates existing keys, `get` retrieves values, `remove` deletes keys.

## Time Complexity
- `put`: O(n/k)
- `get`: O(n/k)
- `remove`: O(n/k)  
*(n = number of keys, k = number of buckets)*

## Space Complexity
- O(n)

## Key Learnings
- Implementing a HashMap from scratch
- Collision handling
- Reference vs index deletion in Python lists

## File
- `706_design_hashmap.py`


