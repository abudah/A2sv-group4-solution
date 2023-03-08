from collections import defaultdict
class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        count=defaultdict(int)
        back=0
        front=0
        res=0
        while front<len(s):
            count[s[front]]+=1
            while (front-back+1)-max(count.values())>k:
                count[s[back]]-=1
                back+=1
            res=max(res,front-back+1)
            front+=1
        return res 