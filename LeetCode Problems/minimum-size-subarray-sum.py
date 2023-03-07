class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        back=0
        front=0
        tot=0
        size=10000000000000
        while front<len(nums)+1:
            while tot<target and front<len(nums):
                tot+=nums[front]
                front+=1
            if tot>=target:
                size=min(size,front-back)
                tot-=nums[back]
                back+=1
            else:
                front+=1
        if size==10000000000000:
            return 0
        else:
            return size        