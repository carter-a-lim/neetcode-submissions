class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        m = 0
        for i in range(len(prices)):
            gain = max(prices[i:]) - prices[i]
            if gain > m:
                m = gain
        return m
