class Solution:
    def countBits(self, n: int) -> List[int]:
        ret = []
        for i in range(0,n+1):
            bits = bin(i)
            count =Counter(bits)
            ret.append(count['1'])
        return ret
        
