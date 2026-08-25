class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        numSet = set(nums)
        maxLen = 0
        res = 1
        sequences = defaultdict(set) # start
        for i in range(len(nums)):
            if nums[i] - 1 not in numSet:
                # start of sequence
                res = 1
                while nums[i] + res in numSet:
                    res += 1

                maxLen = max(maxLen, res)

        return maxLen
