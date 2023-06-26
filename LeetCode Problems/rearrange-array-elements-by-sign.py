class Solution:
    def rearrangeArray(self, nums: List[int]) -> List[int]:
        posNum = []
        negNum = []
        for i in nums:
            if i < 0:
                negNum.append(i)
            else:
                posNum.append(i)
        result = []
        for i in range(len(nums)//2):
            result.append(posNum[i])
            result.append(negNum[i])
        return result