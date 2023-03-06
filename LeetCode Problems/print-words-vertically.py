class Solution:
    def printVertically(self, s: str) -> List[str]:
        listed=s.split()
        maxes=0
        for i in listed:
            maxes=max(maxes,len(i))
        for i in range(len(listed)):
            if len(listed[i])!=maxes:
                listed[i]+=" "*(maxes-len(listed[i]))
        vertical=[]
        for i in range(maxes):
            word=""
            for j in range(len(listed)):
                word+=listed[j][i]
            word=word.rstrip()
            vertical.append(word)
        return vertical

                