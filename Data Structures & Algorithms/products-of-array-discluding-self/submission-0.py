class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        pre = [0] * len(nums)
        pre[0] = nums[0]
        post = [0] * len(nums)
        post[len(post) - 1] = nums[len(nums) - 1]

        
        for i in range(1, len(nums) - 1):
            pre[i] = pre[i - 1] * nums[i]
        for i in range(len(nums) - 2, 0, -1):
            post[i] = post[i + 1] * nums[i]

        res = []
        res.append(post[1])
        for i in range(1, len(nums) - 1):
            res.append(post[i + 1] * pre[i - 1])
        res.append(pre[len(nums) - 2])
        return res