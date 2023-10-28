class Solution:
    def maximumTripletValue(self, nums: List[int]) -> int:
        maxLeft = [nums[0]]
        maxRight = [nums[-1]]
        for i in range(1, len(nums)):
            if nums[i] > maxLeft[-1]:
                maxLeft.append(nums[i])
            else:
                maxLeft.append(maxLeft[-1])
        for i in range(len(nums) - 2, -1, -1):
            if nums[i] > maxRight[-1]:
                maxRight.append(nums[i])
            else:
                maxRight.append(maxRight[-1])
        maxRight.reverse()
        res = -1e9
        for i in range(1, len(nums) - 1):
            val = (maxLeft[i - 1] - nums[i])* maxRight[i + 1]
            res = max(res, val)
        if res > 0:
            return res
        return 0