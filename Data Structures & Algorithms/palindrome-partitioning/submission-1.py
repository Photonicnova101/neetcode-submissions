class Solution:
    def partition(self, s: str) -> List[List[str]]:
        res = []
        def backtrack(start,stop,stack):
            if stop==len(s)-1:
                if s[start:stop+1]==s[start:stop+1][::-1]:
                    res.append(stack.copy()+[s[start:stop+1]])
                    return 
                else:
                    return 

            if s[start:stop+1] == s[start:stop+1][::-1]:
                stack.append(s[start:stop+1])
                backtrack(stop+1,stop+1,stack)
                stack.pop()
            backtrack(start,stop+1,stack)
        backtrack(0,0,[])
        return res


                

