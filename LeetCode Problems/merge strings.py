class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        length1=len(word1)
        length2=len(word2)
        mergedString=''
        index=0
        while index < length1 and index < length2 :
            mergedString+=word1[index]+word2[index]
            index+=1
        if index!=length1:
            mergedString+=word1[index:]
        else:
            mergedString+=word2[index:]
        return mergedString