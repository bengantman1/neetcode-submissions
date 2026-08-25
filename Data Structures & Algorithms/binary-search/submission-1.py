class Solution:
    def search(self, nums: List[int], target: int) -> int:
        r = len(nums) - 1
        l = 0

        while r >= l:
            center = (r + l) // 2
            if nums[center] == target:
                return center
            if target < nums[center]:
                r = center - 1
            else:
                l = center + 1
        return -1