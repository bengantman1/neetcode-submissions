class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        n = len(cost)
        memo = [0] * n
        def recur(i):
            if i > n:
                return float('inf')
            if i == n:
                return 0
            if memo[i]:
                return memo[i]
            c1 = recur(i + 1)
            c2 = recur(i + 2)
            memo[i] = min(c1, c2) + cost[i]
            return memo[i]

        c1 = recur(0)
        c2 = recur(1)
        return min(c1, c2)