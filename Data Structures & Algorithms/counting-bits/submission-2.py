class Solution:
    def countBits(self, n: int) -> List[int]:
        if n == 2:
            return [0, 1, 1]
        res = [0] * (n + 1)
        
        nearest = 2
        for i in range(1, n + 1):
            if i == nearest * 2:
                nearest *= 2
            res[i] = res[i - nearest] + 1

        return res