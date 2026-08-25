class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        res = []

        nums.sort()

        for i in range(len(nums) - 1):
            target = -1 * nums[i]
            l = i + 1
            r = len(nums) - 1
            if nums[i] > 0:
                break
            if i > 0 and nums[i] == nums[i-1]: 
                continue

            while l < r:
                tot = nums[l] + nums[r]
                if tot == target:
                    res.append([nums[i], nums[l], nums[r]])
                    r -= 1
                    l += 1
                    while l < r and nums[l] == nums[l - 1]:
                        l += 1
                    while l < r and nums[r] == nums[r + 1]:
                        r -= 1

                elif tot > target:
                    r -= 1
                else:
                    l += 1

        return res