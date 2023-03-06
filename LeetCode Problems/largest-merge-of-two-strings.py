class Solution:
    def largestMerge(self, word1: str, word2: str) -> str:
    
        index1=0
        index2=0
        merge=""
        while index1<len(word1) and  index2<len(word2):
            if word1[index1:]<word2[index2:]:
                merge+=word2[index2]
                index2+=1
            else:
                merge+=word1[index1]
                index1+=1
        merge+=word1[index1:]
        merge+=word2[index2:]
        return merge