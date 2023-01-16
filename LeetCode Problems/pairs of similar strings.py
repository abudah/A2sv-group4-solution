class Solution:
    def similarPairs(self, words: List[str]) -> int:
        sum=0
        for i,wo1 in enumerate(words):
            for wo2 in words[i+1:]:
                if set(wo1)==set(wo2):
                    sum+=1
        return sum
    