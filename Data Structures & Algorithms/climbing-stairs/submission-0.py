class Solution:
    def climbStairs(self, n: int) -> int:
        memo = [0] * (n)
        def recur(i):
            if i > n:
                return 0
            if i == n:
                return 1
            if memo[i]:
                return memo[i]
            res = recur(i + 1) + recur(i + 2)
            memo[i] = res
            return res
        return recur(0)
            