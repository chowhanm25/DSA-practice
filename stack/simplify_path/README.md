# 71. Simplify Path

## Problem
Given an absolute Unix-style file path, simplify it and return the canonical path.

### Rules
- "." represents current directory
- ".." represents parent directory
- Multiple slashes are treated as one
- "..." or more dots are treated as normal directory names

## Approach
- Split the path using '/'
- Use a stack
- Ignore empty strings and '.'
- Pop when encountering '..'
- Push valid directory names
- Join stack with '/'

## Time Complexity
O(n)

## Space Complexity
O(n)
