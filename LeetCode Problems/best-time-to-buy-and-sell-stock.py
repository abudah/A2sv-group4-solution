class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        left, right = 0, 0
        max_profit = 0

        # we have used two pointer technique or sliding window technique
        while right < len(prices):
            if prices[left] < prices[right]:
                max_profit = max(max_profit, prices[right] - prices[left]) 
            else:
                left = right
            right += 1

        return max_profit