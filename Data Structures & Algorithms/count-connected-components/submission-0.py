class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        
        num = 0
        adjList = [[] for i in range(n)]

        for n1, n2 in edges:
            adjList[n1].append(n2)
            adjList[n2].append(n1)

        visit = set()
        def dfs(cur):
            if cur in visit:
                return
            visit.add(cur)
            for node in adjList[cur]:
                dfs(node)
            
            return

        
        for i in range(n):
            prevLen = len(visit)
            dfs(i)
            postLen = len(visit)
            if prevLen != postLen:
                num += 1
        return num

            