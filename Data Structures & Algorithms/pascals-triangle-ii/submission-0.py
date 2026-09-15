class Solution:
    def getRow(self, rowIndex: int) -> List[int]:
        triangle = []
        triangle.append([1])
        triangle.append([1,1])

        for i in range(2,rowIndex+1):
            newrow = []
            newrow.append(1)
            for x in range(1,len(triangle[-1])):
                newrow.append(triangle[-1][x-1]+triangle[-1][x])
            newrow.append(1)
            triangle.append(newrow)
        return triangle[rowIndex]
