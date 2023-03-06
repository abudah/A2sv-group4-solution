class Solution:
    def smallerNumbersThanCurrent(self, nums: List[int]) -> List[int]:
        sortedNums=sorted(nums)
        load=defaultdict(int)
        for i in range(len(nums)-1,-1,-1):
            load[sortedNums[i]]=i
        return [load[nums[i]] for i in range(len(nums))]
            