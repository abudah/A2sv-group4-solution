class Solution:
    def shipWithinDays(self, weights: List[int], days: int) -> int:
        def helper(cap):
            curr_days = 1
            total = 0
            for w in weights:
                total += w
                if total > cap:
                    total = w
                    curr_days+=1
                    if curr_days > days:
                        return False
            return True
        low=max(weights)
        high=sum(weights)
        while low <= high:
            mid=(low + high)//2        
            if helper(mid):
                high = mid-1
            else:
                low = mid+1
        return low