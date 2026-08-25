class Solution:
    def rob(self, nums: List[int]) -> int:
        n = len(nums)
        if n == 1:
            return nums[0]
        memo = [-1] * n
        def helper(i, arr):
            if i >= n - 1:
                return 0
            if memo[i] != -1:
                return memo[i]
            # don't rob and go to next or rob and skip the next
            memo[i] = max(helper(i + 2, arr) + arr[i], helper(i + 1, arr))
            return memo[i]


        arr1 = nums[0:n-1]
        arr2 = nums[1:n]
        res1 = helper(0, arr1)
        memo = [-1] * n
        res2 = helper(0, arr2)
        return max(res1, res2)

            
            