class Solution:
    def partition(self, s: str) -> List[List[str]]:
        stack = []
        res = []
        def backtrack(i,j):

            if j>=len(s):
                if i==j:
                    res.append(stack.copy())
                return
            
            if s[i:j+1]==(s[i:j+1])[::-1]:
                stack.append(s[i:j+1])
                backtrack(j+1,j+1)
                stack.pop()
            backtrack(i,j+1)
        backtrack(0,0)
        return res



