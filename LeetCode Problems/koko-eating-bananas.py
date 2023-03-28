class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        def check(mid):
            hours=0
            for i in piles:
                hours+=ceil(i/mid)
            if hours <= h:
                return True
            return False

        temp=0
        left = 1
        right = max(piles)
        while left <= right:
            mid=left+(right-left)//2
            if check(mid):
                right=mid-1
                temp=mid
            else:
                left=mid+1
        return temp
            



