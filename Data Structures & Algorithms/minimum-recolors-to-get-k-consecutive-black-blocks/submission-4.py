class Solution:
    def minimumRecolors(self, blocks: str, k: int) -> int:
        # move right pointer till len = 7
        left = 0
        right = k
        output = k
        for i in range(len(blocks)-k+1):
            wCount = Counter(blocks[left:right])["W"]
            if wCount < output:
                output = wCount
            left += 1
            right += 1
        return output