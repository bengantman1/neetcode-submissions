class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        maxLen = 0

        l = 0
        r = 0

        letters = set()

        while r < len(s):
            if s[r] in letters:
                while l <= r:
                    if s[l] != s[r]:
                        letters.remove(s[l])
                        l += 1
                    else:
                        l += 1
                        break

            else:
                letters.add(s[r])
                maxLen = max(maxLen, r - l + 1)
            r += 1
        return maxLen