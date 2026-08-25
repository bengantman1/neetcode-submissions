class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        freqs = [0] * 26
        for c in s:
            idx = ord(c) - ord('a')
            freqs[idx] += 1
        for c in t:
            idx = ord(c) - ord('a')
            freqs[idx] -= 1

        for n in freqs:
            if n != 0:
                return False

        return True