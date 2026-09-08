class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        top,bot=0,len(matrix)-1

        while top<=bot:
            midrow = (top+bot)//2
            if target>matrix[midrow][-1]:
                top=midrow+1
            elif target<matrix[midrow][0]:
                bot=midrow-1
            else:
                break
        
        if not(top<=bot):
            return False
        
        l,r=0,len(matrix[0])
        row = (top+bot)//2
        while l<=r:
            mid = (l+r)//2

            if target>matrix[row][mid]:
                l=mid+1
            elif target<matrix[row][mid]:
                r= mid-1
            else:
                return True
        return False
