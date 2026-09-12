class Solution:
    def isMonotonic(self, nums: List[int]) -> bool:
        increasing = True
        decreasing = True
        if len(nums)==1:
            return True
        for i in range(1,len(nums)):
            if not nums[i-1]<=nums[i]:
                increasing = False
        for i in range(1,len(nums)):
            if not nums[i-1]>=nums[i]:
                decreasing = False
        return increasing or decreasing
