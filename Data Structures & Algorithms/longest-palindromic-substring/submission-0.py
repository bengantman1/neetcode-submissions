class Solution:
    def longestPalindrome(self, s: str) -> str:
        resLen = 0
        resl = -1
        resr = -1
        for i in range(len(s)):
            l = i
            r = i
            
            while l >= 0 and r < len(s) and s[l] == s[r]:
                if (r - l + 1) > resLen:
                    resl = l
                    resr = r
                    resLen = r - l + 1
                l -= 1
                r += 1
                
            l = i
            r = i + 1
            while l >= 0 and r < len(s) and s[l] == s[r]:
                if (r - l + 1) > resLen:
                    resl = l
                    resr = r
                    resLen = r - l + 1
                l -= 1
                r += 1
        return s[resl: resr + 1]
