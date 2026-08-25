class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        
        numset = set(nums)
      

        max_len = 0
        for num in nums:
            if num - 1 not in numset: # beginning of sequence
                i = num + 1
                length = 1
                while i in numset:
                    length += 1
                    i += 1

                if length > max_len:
                    max_len = length

        return max_len
