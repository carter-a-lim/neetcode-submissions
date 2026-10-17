class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        ret = []
        nums.sort()

        #for num in list, l/r on remaining elements, if num[i] == num[i-1], skip it

        for i, num in enumerate(nums):
            if i > 0 and num == nums[i-1]:
                continue
            
            l,r = i+1, len(nums)-1

            while l < r:
                threesum = num + nums[l] + nums[r]
                if threesum > 0:
                    r-=1
                elif threesum < 0: 
                    l +=1
                else:
                    ret.append([num, nums[l], nums[r]])
                    l+=1
                    while nums[l] == nums[l-1] and l<r:
                        l+=1

        return ret
                
