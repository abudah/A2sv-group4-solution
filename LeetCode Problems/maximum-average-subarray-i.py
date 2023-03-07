class Solution:
    def findMaxAverage(self, nums: List[int], k: int) -> float:
        first=0
        second=k
        winSum=sum(nums[:k])
        maxSum=winSum/k
        while second<len(nums):
            winSum=winSum-nums[first]+nums[second]
            maxSum=max(winSum/k,maxSum)
            second+=1
            first+=1
        return maxSum
