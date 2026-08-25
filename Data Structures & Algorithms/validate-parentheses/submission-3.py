class Solution:
    def isValid(self, s: str) -> bool:
        match = {')': '(', '}': '{', ']': '['}

        stack = [] # stack should only have opening parentheses

        for c in s:
            if c in match: # c is a closing parenthesis
                if not stack:
                    return False
                opening = stack.pop()
                
                if match[c] != opening:
                    return False
            else: # c is an opening parenthesis
                stack.append(c)
        if stack:
            return False
        return True
