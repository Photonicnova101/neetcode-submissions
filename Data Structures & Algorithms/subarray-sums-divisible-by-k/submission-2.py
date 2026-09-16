class Solution:
    def subarraysDivByK(self, nums: List[int], k: int) -> int:
        #x is the starting position
        prefix = [0 for _ in range(len(nums)+1)]
        rem_seen = {0:1}
        res=0
        for i in range(len(nums)):
            prefix[i+1] = prefix[i]+nums[i]
            rem = prefix[i+1]%k
            rem_seen[rem] = rem_seen.get(rem,0)+1
        for val in rem_seen.values():
            res+= val*(val-1)//2
        return res

        



