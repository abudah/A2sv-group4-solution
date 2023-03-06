class Solution:
    def minDeletionSize(self, strs: List[str]) -> int:
        count=0
        for i in range(len(strs[0])):
            word=""
            for j in range(len(strs)):
                word+=strs[j][i]
            sortedWord=''.join(sorted(word))
            if sortedWord!=word:
                count+=1
        return count