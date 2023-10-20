class TrieNode():
    def __init__(self):
        self.children = [None]*26

def countDistinctSubstrings(s):
    res = [1]
    def insert(word, root):
        curr = root
        for cr in word:
            idx = ord(cr) - ord('a')
            if not curr.children[idx]:
                curr.children[idx] = TrieNode()
                res[0] += 1
            curr = curr.children[idx]


    root = TrieNode()
    for i in range(len(s)):
        insert(s[i:], root)
    return res[0] 
