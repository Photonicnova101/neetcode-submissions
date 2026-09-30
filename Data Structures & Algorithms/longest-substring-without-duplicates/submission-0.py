class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        if not s:
            return 0
        if len(s)==1:
            return 1
        l,r = 0,1
        longest = 0
        chars = set()
        chars.add(s[l])
        while r<len(s):
            if s[r] in chars:
                while s[r] in chars:
                    chars.remove(s[l])
                    l+=1
            chars.add(s[r])
            longest = max(longest,r-l+1)
            r+=1
        return longest

        