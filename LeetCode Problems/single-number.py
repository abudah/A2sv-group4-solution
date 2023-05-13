class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        tot = 0
        for i in nums:
            tot^= i
        return tot