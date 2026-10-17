class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        mini = prices[0]
        output = 0

        for price in prices:
            if price < mini:
                mini = price

            if price - mini > output:
                output = price - mini

        return output