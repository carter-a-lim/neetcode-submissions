class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        diff = 0
        sm = prices[0]

        for i,p in enumerate(prices):
            gain = p-sm
            if gain > diff:
                diff = gain
            
            if p < sm:
                sm=p
        return diff