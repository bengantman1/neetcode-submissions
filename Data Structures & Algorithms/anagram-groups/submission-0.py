class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        # hashmap from letter counts to word array
        counts = defaultdict(list)
        for i, word in enumerate(strs):
            letters = [0] * 26 
            for c in word:
                index = ord(c) - ord('a')
                letters[index] += 1
            
            counts[tuple(letters)].append(word)
            
        return list(counts.values())
