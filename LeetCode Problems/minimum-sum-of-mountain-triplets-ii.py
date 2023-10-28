class Solution:
    def minimumSum(self, nums: List[int]) -> int:
        minLeft = [nums[0]]
        minRight = [nums[-1]]


        for i in range(1, len(nums)):
            if nums[i] < minLeft[-1]:
                minLeft.append(nums[i])
            else:
                minLeft.append(minLeft[-1])

        for i in range(len(nums) - 2, -1, -1):
            if nums[i] < minRight[-1]:
                minRight.append(nums[i])
            else:
                minRight.append(minRight[-1])
        minRight.reverse()

        res = 1e9

        for i in range(len(nums)):
            if nums[i] > minLeft[i] and nums[i] > minRight[i]:
                triplets = nums[i] + minLeft[i] + minRight[i]
                res = min(res, triplets)
        if res!= 1e9:
            return res
            
        return -1
            



        