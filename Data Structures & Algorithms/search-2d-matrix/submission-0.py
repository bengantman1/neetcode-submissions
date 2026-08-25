class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        l = 0
        cols = len(matrix[0])
        rows = len(matrix)
        r = rows * cols - 1
        rowcol = lambda i: (i // cols, i - cols * (i // cols))
        while l <= r:
            center = (l + r) // 2
            row, col = rowcol(center)
            if matrix[row][col] == target:
                return True
            if matrix[row][col] < target:
                l = center + 1
            else:
                r = center - 1

        return False