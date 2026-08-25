class Solution:
    def findMin(self, nums: List[int]) -> int:
        l = 0
        r = len(nums) - 1
        m = 0
        
        while l < r:

            
            m = (l + r) // 2
           
            if nums[m] > nums[r]:
                # min is to the right of m
                l = m + 1
            else:
                # middle is less than all nums to the right, so min is to the left of middle   
                r = m

                    
        return nums[l]