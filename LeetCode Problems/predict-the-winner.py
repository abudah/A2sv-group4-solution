class Solution:
    def PredictTheWinner(self, nums: List[int]) -> bool:
        def predict(i,j):
            if i==j:
                return nums[i]
            left=nums[i]-predict(i+1,j)
            right=nums[j]-predict(i,j-1)
            return max(left,right)
        return predict(0,len(nums)-1)>=0