class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        #i think i can group these together, so that if i pass once, then the next iteration would see the elements in a group and go use the sequential property of the group


        #another prob simpler and faster way would be to simply sort and then use a sliding window
        nums.sort()
        snums = list(set(nums))
        longest = 1
        curr = 1
        snums.sort()
        print(snums)
        if not nums:
            return 0
        for i in range(len(snums)-1):
            longest = max(longest,curr)
            if snums[i]+1==snums[i+1]:
                curr+=1
                longest = max(longest,curr)
            else:
                longest = max(longest,curr)
                curr=1
        return longest
            
            


        