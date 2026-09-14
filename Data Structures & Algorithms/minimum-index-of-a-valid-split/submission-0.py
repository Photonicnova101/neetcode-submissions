class Solution:
    def minimumIndex(self, nums: List[int]) -> int:
        for i in range(len(nums)-1):
            countfirsth = Counter(nums[0:i+1])
            countsecondh = Counter(nums[i+1:])
            domelm1 = -1
            domelm2 = -2
            sortedfirst = sorted(countfirsth.items(),key =lambda item:item[1],reverse=True)
            sortedsecond = sorted(countsecondh.items(),key =lambda item:item[1],reverse=True)
            
            firstelm,firstfreq = sortedfirst[0]
            secondelm,secondfreq = sortedsecond[0]

            if firstfreq>(i+1)//2:
                domelm1 = firstelm
            if secondfreq>(len(nums)-i-1)//2:
                domelm2= secondelm
            if domelm1==domelm2:
                return i
        return -1