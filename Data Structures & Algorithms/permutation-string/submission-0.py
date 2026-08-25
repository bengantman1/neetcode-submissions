class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        windowLen = len(s1)
        if windowLen > len(s2):
            return False

        freqs = [0] * 26
        for c in s1:
            freqs[ord(c) - ord('a')] += 1
        
        compare = [0] * 26
        r = 0
        while r < len(s1) - 1:
            compare[ord(s2[r]) - ord('a')] += 1
            r += 1
        print(freqs)
        print(compare)
        l = 0
        for r in range(len(s1) - 1, len(s2)):
            compare[ord(s2[r]) - ord('a')] += 1
            if compare == freqs:
                return True
            compare[ord(s2[l]) - ord('a')] -= 1
            l += 1
        return False
