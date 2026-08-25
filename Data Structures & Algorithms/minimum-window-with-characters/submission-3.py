class Solution:
    def minWindow(self, s: str, t: str) -> str:
        countS = {}
        countT = {}

        res = ""
        have = 0
        

        if len(s) < len(t):
            return res

        for i in range(len(t)):
            countS[s[i]] = countS.get(s[i], 0) + 1
            countT[t[i]] = countT.get(t[i], 0) + 1
        for k, v in countT.items():
            if countS.get(k, 0) >= v:
                have += 1 # num of counts that match. num distinct letters in t
        
        need = len(countT)
        if have == need:
            res = s[:len(t)]
        l = 0
        for r in range(len(t), len(s)):

            # update count of substring of s
            
            # check if t is in substring of s by comparing counts
            # if not, increment right pointer
            # if it is, increment left pointer until it is not
            # record substring if it is shorter than previous result
            
            countS[s[r]] = countS.get(s[r], 0) + 1

            if s[r] in countT:
                if countS[s[r]] == countT.get(s[r], 0):
                    have += 1
                if have == need:
                    while s[l] not in countT or countS[s[l]] > countT[s[l]]:
                        countS[s[l]] -= 1
                        l += 1
                        
                    if r - l + 1 < len(res) or res == "":
                        res = s[l:r + 1]
        return res




