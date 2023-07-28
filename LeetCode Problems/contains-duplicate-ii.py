class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
        collect = defaultdict(int)
        front = 0
        while front < len(nums):
            if nums[front] in collect:
                if abs(collect[nums[front]] - front) <= k:
                    return True
            collect[nums[front]] = front
            front += 1
        return False
