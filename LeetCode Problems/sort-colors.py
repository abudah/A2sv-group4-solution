class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        r,w,b=0,0,0
        for i in nums:
            if i==0:
                r+=1
            elif i==1:
                w+=1
            else:
                b+=1
        print(r,w,b)
        for i in range(r):
            nums[i]=0
        for j in range(r,w+r):
            nums[j]=1
        for k in range(r+w, r+b+w):
            nums[k]=2
        return nums