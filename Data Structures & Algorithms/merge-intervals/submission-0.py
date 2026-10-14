class Solution:

    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        intervals.sort()
        res = []
        if len(intervals)==1:
            return intervals
        res.append(intervals[0])
        if len(intervals)>1:
            for interval in intervals[1:]:
                if interval[0]<=res[-1][1]:
                    res[-1]=[res[-1][0],max(interval[1],res[-1][1])]
                else:
                    res.append(interval)
        return res



            
            
        
            