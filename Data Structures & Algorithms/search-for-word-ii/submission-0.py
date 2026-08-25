class Solution:
    def findWords(self, board: List[List[str]], words: List[str]) -> List[str]:
        trie = Trie(words)

        
        root = TrieNode()
        res = set()
        visited = set()
        def backtrack(r, c, cur, word):
            if r < 0 or c < 0 or r >= len(board) or c >= len(board[0]) or (r, c) in visited or board[r][c] not in cur.children:
                return 
            
            visited.add((r, c))
            node = cur.children[board[r][c]]
            word += board[r][c]
            if node.word:
                res.add(word)
            

            backtrack(r + 1, c, node, word)
            backtrack(r, c - 1, node, word)
            backtrack(r - 1, c, node, word)
            backtrack(r, c + 1, node, word)     
            visited.remove((r, c))       

        for r in range(len(board)):
            for c in range(len(board[0])):
                backtrack(r, c, trie.root, "")
            
        return list(res)
            

            

class TrieNode:
    def __init__(self):
        self.children = {}
        self.word = False
       
class Trie:
    def __init__(self, words):
        self.root = TrieNode()
        for word in words:
            cur = self.root
            for c in word:
                if c not in cur.children:
                    cur.children[c] = TrieNode()
                cur = cur.children[c]
            cur.word = True