class Solution:
    def arrangeCoins(self, n: int) -> int:
        # 1, 3, 6, 10, 15
        # +2, +3 +4 +5
        level = 0
        cost = 1
        while n >= cost:
            n -= cost
            level += 1
            cost += 1
        return level
            