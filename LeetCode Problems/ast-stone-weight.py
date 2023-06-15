class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        stones_weight = [-i for i in stones]
        heapq.heapify(stones_weight)
        while len(stones_weight) > 1:
            heapq.heappush(stones_weight, heapq.heappop(stones_weight) - heapq.heappop(stones_weight))
        return -stones_weight[0]