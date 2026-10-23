class Solution:
    def maxArea(self, heights: List[int]) -> int:
        #start with pointer on left and right, for smaller post, move in 
        #bc moving bigger would guarentee no increase

        out=0

        l,r=0,len(heights)-1

        while l<r:
            out = max(out, (r-l)*min(heights[l], heights[r]))

            if heights[r] < heights[l]:
                r -= 1
            else:
                l += 1

        return out