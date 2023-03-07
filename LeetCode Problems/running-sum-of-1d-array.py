class Solution:
    def runningSum(self, nums: List[int]) -> List[int]:
        pref_sum=[nums[0]]
        for i in range(1,len(nums)):
            pref_sum.append(pref_sum[-1]+nums[i])
        return pref_sum