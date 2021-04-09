class Solution:
    def maxProfit(self, prices: List[int]) -> int:

        l_idx = 0
        max_profit = 0

        for i in range(1, len(prices)):
            if prices[i] < prices[l_idx]:
                l_idx = i

            else:
                max_profit = max(max_profit, prices[i] - prices[l_idx])

        return max_profit