class Solution:
    def isHappy(self, n: int) -> bool:
        visited = set()

        def helper(num):
            if num == 1:
                return True
            if num in visited:
                return False
            visited.add(num)
            prod = 0
            for c in str(num):
                prod += int(c) ** 2
            return helper(prod)
        return helper(n)