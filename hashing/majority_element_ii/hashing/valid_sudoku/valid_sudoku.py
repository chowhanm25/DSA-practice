class ValidSudoku:
    """
    Class to validate a 9x9 Sudoku board.

    Rules:
        1. Each row must contain digits 1-9 without repetition.
        2. Each column must contain digits 1-9 without repetition.
        3. Each 3x3 sub-box must contain digits 1-9 without repetition.
    """

    def is_valid(self, board: list[list[str]]) -> bool:
        """
        Validate a 9x9 Sudoku board.

        Args:
            board (list[list[str]]): 2D list representing the Sudoku board. Empty cells are '.'.

        Returns:
            bool: True if board is valid, False otherwise
        """

        rows = set()
        cols = set()
        boxes = set()

        for r in range(9):
            for c in range(9):
                value = board[r][c]
                if value == ".":
                    continue

                row_key = (r, value)
                col_key = (c, value)
                box_key = (r // 3, c // 3, value)

                if row_key in rows or col_key in cols or box_key in boxes:
                    return False

                rows.add(row_key)
                cols.add(col_key)
                boxes.add(box_key)

        return True

