class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        rowset = [set() for _ in range(9)]
        colset = [set() for _ in range(9)]
        squareset = [set() for _ in range(9)]

        for row in range(9):
            for col in range(9):
                val = board[row][col]
                if val == ".": 
                    continue
                if val in rowset[row] or val in colset[col]:
                    return False
                if val in squareset[(row // 3) * 3 + col // 3]:
                    return False
                rowset[row].add(val)
                colset[col].add(val)
                squareset[(row // 3) * 3 + col // 3].add(val)
        return True

