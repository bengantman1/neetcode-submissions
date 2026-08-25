class Solution:
    def search(self, nums: List[int], target: int) -> int:
        
        l = 0
        r = len(nums) - 1

        while l <= r:
            m = (l + r) // 2

            if nums[m] == target:
                return m
            
            if nums[m] > nums[r]:
                # start is to the right
                if nums[m] < target or target <= nums[r]:
                    # all greater nums must be to the right
                    # and if the target is less than the right num
                    l = m + 1
                # smaller nums can be to the left or right
                else:
                    r = m - 1
            else:
                # between m and r is sorted, start is to the left
                # [5, 6, 1, 2, 3, 4]
                # [6, 7, 8, 9, 1m, 2, 3, 4]
                if nums[m] < target and target <= nums[r]:
                    l = m + 1
                else:
                    r = m - 1
            


        return -1