class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        if digits == "":
            return []
        letters = {'2': ['a', 'b', 'c'],
                    '3': ['d', 'e', 'f'],
                    '4': ['g', 'h', 'i'],
                    '5': ['j', 'k', 'l'],
                    '6': ['m', 'n', 'o'],
                    '7': ['p', 'q', 'r', 's'],
                    '8': ['t', 'u', 'v'],
                    '9': ['w', 'x', 'y', 'z']
                    }
        res = []
        def backtrack(i, choices):
            if i >= len(digits):
                res.append(choices)
                return
            for c in letters[digits[i]]:
                choices += c
                backtrack(i + 1, choices)
                choices = choices[0:len(choices) - 1]


        choices = ''
        backtrack(0, choices)
        return res