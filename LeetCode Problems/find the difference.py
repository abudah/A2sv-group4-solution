class Solution:
    def findTheDifference(self, s: str, t: str) -> str:
        dictionaryT={}
        dictionaryS={}
        for i in s:
            if i in dictionaryS.keys():
                dictionaryS[i]+=1
            else:
                dictionaryS[i]=1
        for i in t:
            if i in dictionaryT.keys():
                dictionaryT[i]+=1
            else:
                dictionaryT[i]=1
        for key,values in dictionaryT.items():
            if key not in dictionaryS.keys():
                return key
            if values!=dictionaryS[key]:
                return key 
        