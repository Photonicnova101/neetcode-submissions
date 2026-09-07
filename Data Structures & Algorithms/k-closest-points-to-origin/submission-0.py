class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
          #organize the minheap by distance and use tuples for (distance,index)
        minheap = []
        for index,coords in enumerate(points):
            xi = coords[0]
            yi = coords[1]
            distance = (pow(xi,2))+(pow(yi,2))
            minheap.append((distance,index))

        heapq.heapify(minheap)
        result=[]
        for _ in range(k):
            distance,index = heapq.heappop(minheap)
            result.append(points[index])
        return result

            
