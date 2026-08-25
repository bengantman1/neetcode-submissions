class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        results = {} # frequencies set : list of words
        for word in strs:
            freqs = [0] * 26
            for c in word:
                freqs[ord(c) - ord('a')] += 1
            freqs = tuple(freqs)
            if freqs not in results:
                results[freqs] = [word]
            else:
                results[freqs].append(word)
        res = []
        for words in list(results.values()):
            res.append(words)

        return res