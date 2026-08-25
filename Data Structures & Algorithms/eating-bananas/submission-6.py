class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        r = max(piles)
        l = 1
        # binary search for correct k in range [l, r]

        k = r

        while r >= l:
            m = (r + l) // 2

            hoursM = 0
            for pile in piles:
                hoursM += pile // m
                if pile % m:
                    hoursM += 1
            if hoursM > h:
                l = m + 1
            else:
                
                k = m
                r = m - 1

        return k
            