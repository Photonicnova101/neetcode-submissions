class Solution:
    def maxArea(self, heights: List[int]) -> int:
        l=0
        r=len(heights)-1
        res=0
        #as we traverse through heights on the right we can trap a maxarea of the min(maxheight on the left and nums[r])*width
        #otherwise we will have 
        while l<r:
            area = min(heights[l],heights[r])*(r-l)
            res = max(res,area)
            if heights[l]<=heights[r]:
                l+=1
            else:
                r-=1
        return res
            
            
