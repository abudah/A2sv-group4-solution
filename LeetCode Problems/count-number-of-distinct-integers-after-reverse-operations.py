class Solution:
    def countDistinctIntegers(self, nums: List[int]) -> int:
        reversedDigits=[]
        for i in nums:
            reversedDigits.append(int(str(i)[::-1]))
        nums.extend(reversedDigits)
        return len(set(nums))