class Solution:
    def partition(self, s: str) -> List[List[str]]:
        def isPalindrome(i, j):
            l = i
            r = j
            while l < r:
                if s[l] != s[r]:
                    return False
                l += 1
                r -= 1
            return True

        partition = []
        res = []
        def helper(i):
            if i >= len(s):
                res.append(partition.copy())
                return
            for j in range(i, len(s)):
                if isPalindrome(i, j):
                    partition.append(s[i:j+1])
                    helper(j + 1)
                    partition.pop()
        helper(0)
        return res