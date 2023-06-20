class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        num = [-i for i in nums]
        heapq.heapify(num)
        return (-heapq.heappop(num)-1)*(-heapq.heappop(num)-1)