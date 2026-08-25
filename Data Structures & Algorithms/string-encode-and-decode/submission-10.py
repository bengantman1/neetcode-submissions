class Solution:

    def encode(self, strs: List[str]) -> str:
        res = ""
        for word in strs:
            length = len(word)
            res += (str(length) + '#' + word)
        return res
        


    def decode(self, s: str) -> List[str]:
        l = 0
        r = 0
        res = []
        while r < len(s):
            while (s[r] != '#'):
                r += 1
            length = int(s[l:r])
            l = r + 1
            r += length + 1
            res.append(s[l:r])
            l = r

        return res
            
            