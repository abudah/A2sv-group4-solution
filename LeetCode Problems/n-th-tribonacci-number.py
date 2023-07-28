class Solution:
    def tribonacci(self, n: int) -> int:
        dp = defaultdict(int)

        def tri(i):
            if i == 0 or i == 1:
                return i
            if i== 2:
                return 1    

            if i in dp:
                return dp[i]

            res = tri(i-1) + tri(i-2) + tri(i-3)
            dp[i] = res
            return res
            
        return tri(n)