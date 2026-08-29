class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        maxones = 0
        curr = 0
        for i in nums:
            if i==1:
                curr+=1
                maxones = max(maxones,curr)
            else:
                curr=0
        return maxones

        