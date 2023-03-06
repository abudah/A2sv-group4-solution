class Solution:
    def applyOperations(self, nums: List[int]) -> List[int]:
        for i in range(len(nums)-1):
            if nums[i]==nums[i+1]:
                nums[i]=nums[i]*2
                nums[i+1]=0
        Zeros=nums.count(0)
        withoutZeros=[i for i in nums if i!=0]
        return withoutZeros+[0]*Zeros