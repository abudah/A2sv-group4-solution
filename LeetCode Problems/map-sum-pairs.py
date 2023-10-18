class TrieNode():
    def __init__(self):
        self.value = 0
        self.children = [None for i in range(26)]


class MapSum:

    def __init__(self):
        self.root = TrieNode()        

    def insert(self, key: str, val: int) -> None:
        curr = self.root
        for w in key:
            idx = ord(w) - ord('a')
            if not curr.children[idx]:
                curr.children[idx] = TrieNode()
            curr = curr.children[idx]
        curr.value = val
        
        

    def sum(self, prefix: str) -> int:
        res = [0]
        def dfs(node):
            res[0] += node.value
            for el in node.children:
                if el:
                    dfs(el)
        curr = self.root
        for w in prefix:
            idx = ord(w) - ord('a')
            if not curr.children[idx]:
                return 0
            curr = curr.children[idx]
        dfs(curr)
        return res[0]


# Your MapSum object will be instantiated and called as such:
# obj = MapSum()
# obj.insert(key,val)
# param_2 = obj.sum(prefix)