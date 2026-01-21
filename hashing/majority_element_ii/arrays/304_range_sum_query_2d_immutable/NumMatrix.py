class NumMatrix(object):

    def __init__(self, matrix):
        """
        Initializes the prefix sum matrix.

        :type matrix: List[List[int]]
        """
        if not matrix or not matrix[0]:
            self.ps = []
            return

        rows, cols = len(matrix), len(matrix[0])
        self.ps = [[0] * (cols + 1) for _ in range(rows + 1)]

        # Build prefix sum matrix
        for i in range(rows):
            for j in range(cols):
                self.ps[i + 1][j + 1] = (
                    matrix[i][j]
                    + self.ps[i][j + 1]
                    + self.ps[i + 1][j]
                    - self.ps[i][j]
                )

    def sumRegion(self, row1, col1, row2, col2):
        """
        Returns the sum of elements inside the rectangle
        defined by (row1, col1) and (row2, col2).

        :rtype: int
        """
        return (
            self.ps[row2 + 1][col2 + 1]
            - self.ps[row1][col2 + 1]
            - self.ps[row2 + 1][col1]
            + self.ps[row1][col1]
        )

