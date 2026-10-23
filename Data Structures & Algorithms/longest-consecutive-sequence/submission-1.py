class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        # get mins (starting points)
        mins = set()
        nums_set = set(nums)

        for num in nums:
            if num-1 in nums_set:
                continue
            mins.add(num)
        
        print(mins)


        #look for next in set for o(1) lookups for each min (o(n*1) = o(n))
        m = 0
        for num in mins:
            i=1
            while(num+i in nums_set):
                i+=1
            m = max(m, i)

        return m