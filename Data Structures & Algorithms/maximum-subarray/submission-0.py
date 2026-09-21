class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        prefix = 0
        min_prefix = 0          # prefix sum of the empty subarray
        best = float("-inf")

        for num in nums:
            prefix += num
            best = max(best, prefix - min_prefix)  # best subarray ending here
            min_prefix = min(min_prefix, prefix)   # update after using it

        return best
