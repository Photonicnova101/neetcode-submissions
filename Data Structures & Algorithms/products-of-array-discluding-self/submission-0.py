class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        original = nums[:]  # preserve original values
        totalproduct = 1
        zerocount = 0
        for num in original:
            if num != 0:
                totalproduct *= num
            else:
                zerocount += 1

        res = [0] * len(nums)
        for i in range(len(nums)):
            if zerocount > 1:
                res[i] = 0
            elif zerocount == 1:
                res[i] = totalproduct if original[i] == 0 else 0
            else:
                res[i] = totalproduct // original[i]

        return res