class TrieNode():
    def __init__(self):
        self.is_end = False
        self.children = [None]*26
        self.val = None

class Trie():
    def __init__(self):
        self.root = TrieNode()

    def insert(self, word):
        curr= self.root
        for cr in word:
            idx = ord(cr) - ord('a')
            if not curr.children[idx]:
                curr.children[idx] = TrieNode()
            curr = curr.children[idx]
        curr.is_end = True
        curr.val = word
    def searchNode(self, word):
        curr= self.root
        for cr in word:
            idx = ord(cr) - ord('a')
            if not curr.children[idx]:
                return None
            curr = curr.children[idx]
        return curr
    def dfs(self,curr, localRes):
        if len(localRes) == 3:
            return
        if curr.is_end:
            localRes.append(curr.val)
        
        for c in curr.children:
            if c:
                self.dfs(c, localRes)

class Solution:
    def suggestedProducts(self, products: List[str], searchWord: str) -> List[List[str]]:
        root = Trie()
        for word in products:
            root.insert(word)
        localRes = []
        result = []
        for i in range(len(searchWord)):
            curr = root.searchNode(searchWord[:i+ 1])
            if  curr:
                root.dfs(curr, localRes)
            result.append(localRes)
            localRes = []
        return result