class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        numrows = len(grid)
        numcols = len(grid[0])
        numislands = 0
        visited = set()
        for r in range(numrows):
            for c in range(numcols):

                # bfs
                if grid[r][c] == "1" and (r,c) not in visited:
                    q = []
                    q.append((r, c))
                    
                    
                    while q:
                        newr, newc = q.pop(0) 
                        if (newr, newc) not in visited and (0 <= newr < numrows) and (0 <= newc < numcols) and grid[newr][newc] == "1":
                            if newr + 1 < numrows:
                                q.append((newr + 1, newc))
                            
                            if newr - 1 < numrows:
                                q.append((newr - 1, newc))
                            if newc - 1 < numcols:
                                q.append((newr, newc - 1))

                            if newc + 1 < numcols:
                                q.append((newr, newc + 1))

                            visited.add((newr, newc))

                    numislands += 1

        return numislands


