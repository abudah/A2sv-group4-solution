class Solution:
    def countGoodNumbers(self, n: int) -> int:
        mod=1000000007
        def myPow(x,n):
            if n==0:
                return 1
            if n%2==0:
                return myPow(((x%mod)*(x%mod))%mod,n/2)%mod
            return ((x%mod)*myPow(x,n-1)%mod)%mod
            
        odd=n//2
        even=(n+1)//2
        return ((myPow(5,even)%mod)*myPow(4,odd)%mod)%mod
    