class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        numSet = set(nums)
        res = 0
        for i in range(len(nums)):
            if (nums[i] - 1) not in numSet:
                # this num is the start of a sequence
                cur = nums[i]
                length = 0
                while cur in numSet:
                    cur += 1
                    length += 1
                res = max(length, res)
        return res
