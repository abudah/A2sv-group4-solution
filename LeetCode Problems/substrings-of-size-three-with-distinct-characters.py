class Solution:
    def countGoodSubstrings(self, s: str) -> int:
        window_sub= Counter(s[:3])
        back = 0
        res = 0
        for front in range(3, len(s)+1):
            if len(Counter(s[front -3: front]))== 3:
                res += 1
            
        return res
