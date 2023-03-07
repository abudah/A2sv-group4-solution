from collections import Counter

class Solution:
    def findAnagrams(self, s: str, p: str) -> List[int]:
        target=[]
        front=len(p)-1
        back=0
        target_counts=Counter(p)
        window_counts=Counter(s[:front])
        while front<len(s):
            window_counts[s[front]]+=1
            if window_counts==target_counts:
                target.append(back)
            window_counts[s[back]]-=1
            if window_counts[s[back]]==0:
                del window_counts[s[back]]
            back+=1
            front+=1
            
        return target


