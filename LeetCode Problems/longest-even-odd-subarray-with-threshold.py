class Solution:
    def longestAlternatingSubarray(self, nums: List[int], threshold: int) -> int:
        rem = 0
        res = 0
        temp = 0
        for el in nums:
            if el <= threshold and rem == el % 2:
                temp += 1
                rem = 0 if rem else 1
            else:
                res = max(res, temp)
                rem = 0
                temp = 0
                if el <= threshold and rem == el % 2:
                    temp += 1
                    rem = 0 if rem else 1
        return max(res, temp)