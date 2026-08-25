class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        adjList = {i: [] for i in range(numCourses)}
        for crs, pre in prerequisites:
            adjList[crs].append(pre)
        
        cycle = set()
        visit = set()
        output = []

        def dfs(crs):
            if crs in cycle:
                return False
            if crs in visit:
                return True
            
            cycle.add(crs)
            for pre in adjList[crs]:
                if not dfs(pre):
                    return False
            cycle.remove(crs)
            output.append(crs)
            visit.add(crs)
            adjList[crs] = []
            return True

        for crs in range(numCourses):
            if not dfs(crs):
                return []
        return output
            