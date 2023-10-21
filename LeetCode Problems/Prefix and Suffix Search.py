class TrieNode():
    def __init__(self):
        self.positions = []
        self.children = [None] * 26

class Trie():
    def __init__(self):
        self.root = TrieNode()

    def insert(self,word, i):
        curr = self.root
        curr.positions.append(i)
        for cr in word:
            idx = ord(cr) - ord('a')
            if not curr.children[idx]:
                curr.children[idx] = TrieNode()
            curr= curr.children[idx]
            curr.positions.append(i)

    def search(self, word):
        curr = self.root
        for cr in word:
            idx = ord(cr) - ord('a')
            if not curr.children[idx]:
                return []
            curr= curr.children[idx]
        return curr.positions


class WordFilter:

    def __init__(self, words: List[str]):
        self.prefix, self.suffix = Trie(), Trie()

        for i in range(len(words)):
            word2 = words[i][::-1]
            self.prefix.insert(words[i], i)
            self.suffix.insert(word2, i)

    def f(self, pref: str, suff: str) -> int:
        prefs = self.prefix.search(pref)
        suffs = self.suffix.search(suff[::-1])
        pi, si= len(prefs) - 1, len(suffs) - 1
        while pi >= 0 and si >= 0:
            if prefs[pi] > suffs[si]:
                pi -= 1
            elif prefs[pi] < suffs[si]:
                si -= 1
            else:
                return prefs[pi]
        return -1

# Your WordFilter object will be instantiated and called as such:
# obj = WordFilter(words)
# param_1 = obj.f(pref,suff)