class Solution:
    def subsetXORSum(self, nums: List[int]) -> int:
        res =[]
        subsets = []
        def backtrack(i):
            if i==len(nums):
                res.append(subsets[:])
                return 
            
            #exclude nums[i] by continuing 
            backtrack(i+1)
            #include nums[i]
            subsets.append(nums[i])
            #continue with the appendage
            backtrack(i+1)
            #pop this descision after everything above has already been appended to the subsets
            subsets.pop() 
        backtrack(0)
        output = 0
        for arr in res:
            if not arr:
                output+=0
            else:
                Xortot=arr[0]
                for i in range(1,len(arr)):
                    Xortot^=arr[i]
                output+=Xortot
        return output
                    

        