class TrieNode():
    def __init__(self):
        self.count = 1
        self.children = [None]*26 

class Solution:
    def sumPrefixScores(self, words: List[str]) -> List[int]:
        def score(word, root):
            count = 0
            curr = root
            for cr in word:
                idx = ord(cr) - ord('a')
                curr = curr.children[idx]
                count += curr.count
            return count

        def insert(word, root):
            curr = root
            for cr in word:
                idx = ord(cr) - ord('a')
                if not curr.children[idx]:
                    curr.children[idx] = TrieNode()
                else:
                    curr.children[idx].count += 1
                curr = curr.children[idx]
        root = TrieNode()
        for word in words:
            insert(word, root)
        res = []
        for word in words:
            res.append(score(word, root))
        return res

                
            

