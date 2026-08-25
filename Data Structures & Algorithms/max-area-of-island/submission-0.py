class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        rows = len(grid)
        cols = len(grid[0])
        visit = set()
        def dfs(r, c):
            if (r < 0 or c < 0 or r >= rows or c >= cols or not grid[r][c] or (r,c) in visit):
                return 0
            visit.add((r, c))
            return (1 + dfs(r + 1, c) +
                dfs(r - 1, c) +
                dfs(r, c + 1) +
                dfs(r, c - 1))
        maxArea = 0
        
        for r in range(rows):
            for c in range(cols):
                if grid[r][c]:
                    maxArea = max(maxArea, dfs(r, c))
                else:
                    curArea = 0

        return maxArea