class Solution:
    def hammingWeight(self, n: int) -> int:
        out = 0
        for i in range(32):
            if not n:
                break
            
            if n & 1:
                out += 1
            n >>= 1
        return out