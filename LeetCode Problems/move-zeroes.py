class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        seeker=0
        holder=0
        while holder!=len(nums):
            if nums[holder]!=0:
                nums[seeker],nums[holder]=nums[holder],nums[seeker]
                seeker+=1
            holder+=1
        