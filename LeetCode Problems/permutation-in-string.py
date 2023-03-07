from collections import Counter
class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        back=0
        front=len(s1)-1
        target_window=Counter(s1)
        word_window=Counter(s2[:front])
        # print(target_window)
        while front<len(s2):
            word_window[s2[front]]+=1
            if word_window ==target_window:
                return True
            word_window[s2[back]]-=1
            if word_window[s2[back]]==0:
                del word_window[s2[back]]
            back+=1
            front+=1
        return False
        