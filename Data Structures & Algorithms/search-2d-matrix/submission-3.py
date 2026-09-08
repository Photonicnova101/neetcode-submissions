class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        top,bot=0,len(matrix)-1
        #in the top while loop we want to bound the row, so we count the conditions in which we can narrow done the range, we shrink downwards then the ending of the row is less than the target, we shrink upwards when the beginning of the row is greater than the target
        while top<=bot:
            midrow = (top+bot)//2
            if target>matrix[midrow][-1]:
                top=midrow+1
            elif target<matrix[midrow][0]:
                bot=midrow-1
            else:
                break
        #we get the row and then enact binary search upon the resulting row
        if not (top<=bot):
            return False
        row = (top+bot)//2
        l,r=0,len(matrix[0])
        while l<=r:
            mid = (l+r)//2
            if target>matrix[row][mid]:
                l=mid+1
            elif target<matrix[row][mid]:
                r=mid-1
            else:
                return True

        return False
        