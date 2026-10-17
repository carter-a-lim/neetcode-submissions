class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
        # find int, check i+k for same

        for i in range(len(nums)):
            if nums[i] in nums[i+1:i+k+1]:
                return True
        return False