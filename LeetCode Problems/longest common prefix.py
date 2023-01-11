class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        flag=True
        l=0
        word=''
        while flag and l<=len(strs[0]):
            word=strs[0][:l]
            for i in range(1,len(strs)):
                if strs[i].startswith(word):
                    flag=True
                else:
                    flag=False
                    word=word[:-1]
                    break
            l+=1
        return word   