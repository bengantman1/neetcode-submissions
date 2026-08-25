class Solution:
    def rotate(self, matrix: List[List[int]]) -> None:
        
        matrix.reverse()
        n = len(matrix)
        for i in range(1, n):
            for j in range(0, i):
                temp = matrix[j][i]
                matrix[j][i] = matrix[i][j]
                matrix[i][j] = temp
        
        
