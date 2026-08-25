class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
       # [1, 2, 8, 48]
       # [48,48, 24,6]

       # [-1, 0, 0, 0, 0]
       # [0, 0, 6, 6, 3]
        prods = [0] * len(nums)
        total = 1
        zeroCnt = 0
        for num in nums:
            if num != 0:
                total *= num
            else:
                zeroCnt += 1
        i = 0
        if zeroCnt > 1: return prods
        for num in nums:
            if zeroCnt == 1:
                if num == 0:
                    prods[i] = total
                else:
                    prods[i] = 0

            else:
                prods[i] = total // num

            i += 1
        return prods