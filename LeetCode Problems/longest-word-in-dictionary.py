class TrieNode():
    def __init__(self):
        self.is_end = False
        self.children = [None]*26

class Solution:
    def longestWord(self, words: List[str]) -> str:
        root = TrieNode()
        def insert(word, root):
            curr = root
            for cr in word:
                idx = ord(cr) - ord('a')
                if not curr.children[idx]:
                    curr.children[idx] = TrieNode()
                curr = curr.children[idx]
            curr.is_end = True

        for word in words:
            insert(word, root)
        def dfs(word, root):
            curr = root
            # print(word)
            for ind, cr in enumerate(word):
                idx = ord(cr) - ord('a')
                # print(ind, idx, cr)
                if not curr.children[idx].is_end:
                    return ind 
                curr = curr.children[idx]
                
            return len(word)
        store = []
        for word in words:
            l = dfs(word, root)
            store.append([word, l])

        store.sort(key = lambda x:x[1], reverse = True)
        res = [i for i in store if i[1]==store[0][1] and i[1] != 0]
        res.sort()
        return res[0][0] if res else ""
        

            