class TrieNode():
    def __init__(self):
        self.is_end = False
        self.children = [None for i in range(26)]

class Solution:
    def numMatchingSubseq(self, s: str, words: List[str]) -> int:
        def is_subsequence(mainWord, curr, word):
            ind = 0
            for w in mainWord:
                idx = ord(w) - ord('a')
                idy = ord(word[ind]) - ord('a')
                if curr.children[idy] == curr.children[idx]:
                    ind += 1
                if ind == len(word):
                    return True
                curr = curr.children[idx]
            return False

        root = TrieNode()
        curr= root
        for w in s:
            ind = ord(w) - ord('a')
            if not curr.children[ind]:
                curr.children[ind] = TrieNode()
            curr = curr.children[ind]
        curr.is_end = True
        dicts = Counter(words)

        res = 0
        for key, val in dicts.items():
            temp = root
            if is_subsequence(s, temp, key):
                res += val
        
        return res