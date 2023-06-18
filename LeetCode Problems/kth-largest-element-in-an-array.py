class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        numsMax = [-i for i in nums]
        heapq.heapify(numsMax)
        for i in range(k-1):
            heapq.heappop(numsMax)
        return -heapq.heappop(numsMax)