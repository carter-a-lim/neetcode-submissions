class Solution:
    def minimumDifference(self, nums: List[int], k: int) -> int:
        nums.sort()
        left = 0
        right = k-1
        smallest = nums[-1] - nums[0]

        for i in range(len(nums)-k+1):
            spread = nums[right] - nums[left]
            if spread < smallest:
                smallest = spread
            left += 1
            right += 1
        return smallest
