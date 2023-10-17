
class TrieNode:
    def __init__(self):
        self.is_end  = False
        self.children = [None for i in range(26)]

class WordDictionary:
    def __init__(self):
        self.root = TrieNode()

    def addWord(self, word: str) -> None:
        curr = self.root
        for cr in word:
            ind = ord(cr) - ord('a')
            if not curr.children[ind]:
                curr.children[ind] = TrieNode()
            curr = curr.children[ind]
        curr.is_end = True

    def search(self, word: str) -> bool:
        def searching(cur,index):
            if index == len(word):
                return cur.is_end
            ind = ord(word[index]) - ord('a')
            if ind == -51:
                for el in cur.children:
                    if el and searching(el, index + 1):
                            return True
                return False
            else:
                if not cur.children[ind]:
                    return False
                return searching(cur.children[ind], index + 1)
        return searching(self.root, 0)


# Your WordDictionary object will be instantiated and called as such:
# obj = WordDictionary()
# obj.addWord(word)
# param_2 = obj.search(word)