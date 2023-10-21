class TrieNode():
    def __init__(self):
        self.link = [None, None]

class Trie():
    def __init__(self):
        self.root = TrieNode()
    
    def insert(self, num, length):
        curr = self.root
        for i in range(length, -1, -1):
            bit = (num >> i) & 1
            if not curr.link[bit]:
                curr.link[bit] = TrieNode()
            curr = curr.link[bit]

    def getMax(self, num, length):
        curr= self.root
        max_ = 0
        for i in range(length, -1, -1):
            bit = (num >> i) & 1
            if curr.link[1- bit]:
                max_ = max_ | 1 << i
                curr = curr.link[1-bit]
            else:
                curr = curr.link[bit]
        return max_


class Solution:
    def findMaximumXOR(self, nums: List[int]) -> int:
        length = len(bin(max(nums))) -2 
        root = Trie()

        for num in nums:
            root.insert(num, length)
        maximum = 0

        for num in nums:
            maximum = max(maximum, root.getMax(num, length))
        return maximum