class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        counts = defaultdict(int)
        for c in s:
            counts[c] = 1 + counts.get(c, 0)
        for c in t:
            counts[c] = counts.get(c, 0) - 1
        
        for v in counts.values():
            if v != 0:
                return False
        return True
