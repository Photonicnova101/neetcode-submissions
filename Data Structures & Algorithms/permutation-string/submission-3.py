class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        counts1 = Counter(s1)

        l,r = 0,len(s1)
        while l<len(s2):
            if counts1 == Counter(s2[l:r]):
                return True
            else:
                r+=1
                l+=1
            
        return False



