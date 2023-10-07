class Solution:
    def longestEqualSubarray(self, nums: List[int], k: int) -> int:
        sub_array = defaultdict(int)
        front = 0
        back = 0
        res = 0

        while front < len(nums):
            sub_array[nums[front]] += 1
            res = max(res, sub_array[nums[front]])
            if (front - back + 1) - res > k:
                sub_array[nums[back]] -= 1
                back += 1
    
            front += 1
        return res
