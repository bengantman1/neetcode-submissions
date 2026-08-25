class Solution:
    def rob(self, nums: List[int]) -> int:
            
        def helper(arr):
            p1 = 0 # oldest
            p2 = 0 # newest
            for i in range(len(arr)):
                temp = max(p1 + arr[i], p2)
                p1 = p2
                p2 = temp

            return p2
        
        return max(nums[0], helper(nums[:-1]), helper(nums[1:]))



            
            