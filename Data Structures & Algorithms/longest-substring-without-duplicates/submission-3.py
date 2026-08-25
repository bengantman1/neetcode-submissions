class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        if len(s) == 0:
            return 0
        if len(s) == 1:
            return 1

        l = 0
        maxlen = 0
        letterset = set()
        letterset.add(s[l])
        for r in range(1, len(s)):
            if s[r] in letterset:
                while s[l] != s[r]:
                    letterset.remove(s[l])
                    l += 1
                    
                l += 1
            letterset.add(s[r])
            maxlen = max(r - l + 1, maxlen)
            r += 1
        
        return maxlen