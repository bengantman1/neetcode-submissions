class Solution:
    def rob(self, nums: List[int]) -> int:
        n = len(nums)
        if n == 0:
            return nums[0]
        memo = [-1] * n

        def mostRobbed(i):
            if i >= n:
                return 0
            if memo[i] != -1:
                return memo[i]
            memo[i] = max(mostRobbed(i + 1), mostRobbed(i + 2) + nums[i])
            return memo[i]
        
        return mostRobbed(0)