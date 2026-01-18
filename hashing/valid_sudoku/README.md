# Valid Sudoku

This folder contains a Python solution to validate a 9x9 Sudoku board.

## Problem

- Validate that each row, column, and 3x3 sub-box contains digits 1-9 without duplicates.
- Empty cells are represented by `"."` and ignored.

## Approach

- Traverse the board once.
- Use sets to track seen values in rows, columns, and 3x3 boxes.
- Each cell generates:
  - `(row, value)` → checks row duplicates
  - `(col, value)` → checks column duplicates
  - `(box_row, box_col, value)` → checks 3x3 box duplicates
- If any duplicate is found, the board is invalid.

## Usage Example

```python
from valid_sudoku import ValidSudoku

board = [
    ["5","3",".",".","7",".",".",".","."],
    ["6",".",".","1","9","5",".",".","."],
    [".","9","8",".",".",".",".","6","."],
    ["8",".",".",".","6",".",".",".","3"],
    ["4",".",".","8",".","3",".",".","1"],
    ["7",".",".",".","2",".",".",".","6"],
    [".","6",".",".",".",".","2","8","."],
    [".",".",".","4","1","9",".",".","5"],
    [".",".",".",".","8",".",".","7","9"]
]

validator = ValidSudoku()
print(validator.is_valid(board))  # True or False

