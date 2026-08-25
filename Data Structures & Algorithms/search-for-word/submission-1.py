class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        visited = set() # row, col visited
        row_size = len(board)
        col_size = len(board[0])
        def backtrack(i, row, col, visited):
            if i == len(word):
                return True
            if (row >= row_size or col >= col_size or row < 0 or col < 0) or word[i] != board[row][col]:
                return False

            if (row, col) in visited:
                return False
            
            visited.add((row,col))
            res = (backtrack(i + 1, row + 1, col, visited)
            or backtrack(i + 1, row, col + 1, visited)
            or backtrack(i + 1, row - 1, col, visited)
            or backtrack(i + 1, row, col - 1, visited))

            visited.remove((row,col))
            return res

        for r in range(row_size):
            for c in range(col_size):
                if backtrack(0, r, c, visited):
                    return True
        return False