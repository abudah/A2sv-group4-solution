class Solution:
    def maxIceCream(self, costs: List[int], coins: int) -> int:
        prefixSum = 0
        costs.sort()
        if costs[0] > coins: return 0
        for i in range(len(costs)):
            prefixSum += costs[i]
            if prefixSum > coins:
                return i
            
        return len(costs)
        