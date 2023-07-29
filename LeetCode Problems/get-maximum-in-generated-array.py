class Solution:
    def getMaximumGenerated(self, n: int) -> int:
        memo = [0] * (n+1)

        for i in range(n+1):
            if i == 0 or i == 1:
                memo[i] = i
            if i%2 == 0:
                memo[i] = memo[i//2] 
            else:
                memo[i]  =  memo[i//2] +  memo[i//2 + 1]
        
        return int(max(memo))