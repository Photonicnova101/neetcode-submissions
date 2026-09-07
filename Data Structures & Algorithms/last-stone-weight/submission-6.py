class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        if not stones:
            return 0
        for i in range(len(stones)):
            stones[i] = -stones[i]
        heapq.heapify(stones)

        while len(stones)>1:
            max1=heapq.heappop(stones)
            max2=heapq.heappop(stones)
            if max1==max2:
                continue
            else:
                heapq.heappush(stones,-(max(-max1,-max2)-min(-max1,-max2)))
        return -stones[0] if stones else 0 

