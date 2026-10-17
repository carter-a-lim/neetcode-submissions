class Solution:
    def pivotIndex(self, nums: List[int]) -> int:
        i = 0
        for i in range(len(nums)):
            if sum(nums[0:i]) == sum(nums[i+1:]):
                return i

        else: return -1