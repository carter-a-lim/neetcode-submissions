class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
        # for each number, check +k spots for same number

        for i in range(len(nums)):
            if nums[i] in nums[i+1:i+k+1]:
                return True
        return False