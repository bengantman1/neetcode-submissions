class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        if not nums:
            return 0
        nums.sort()
        maxLen = 1
        res = 1
        for i in range(1, len(nums)):
            if nums[i] == nums[i - 1] + 1:
                res += 1
                maxLen = max(maxLen, res)
            elif nums[i] == nums[i - 1]:
                continue
            else:
                res = 1
        return maxLen