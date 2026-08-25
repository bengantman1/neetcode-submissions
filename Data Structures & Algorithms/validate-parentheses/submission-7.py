class Solution:
    def isValid(self, s: str) -> bool:
        mapping = {'}':'{', ']':'[', ')':'('}
        stack = []
        if len(s) <= 1:
            return False

        for c in s:
            if c in mapping.values(): # c is opening
                stack.append(c)
            elif not stack or stack.pop() != mapping[c]:
                return False
        return False if stack else True