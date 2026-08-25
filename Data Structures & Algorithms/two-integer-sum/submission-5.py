class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        have = {}
        have[nums[0]] = 0 # value, idx
        for i in range(1, len(nums)):
            need = target - nums[i]
            if need in have:
                return [have[need], i]
            have[nums[i]] = i

            
