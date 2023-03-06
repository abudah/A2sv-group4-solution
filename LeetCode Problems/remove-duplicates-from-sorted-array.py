class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        target=1
        for i in range(len(nums)-1):
            if nums[i]!=nums[i+1]:
                nums[target]=nums[i+1]
                target+=1
        return target
        