class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        rows = len(board)
        cols = len(board[0])
        visited = [[False for _ in range(cols)] for _ in range(rows)]
        directions = [[1,0],[-1,0],[0,1],[0,-1]]
        def backtrack(r,c,index):
            if index==len(word):
                return True
            if (r<0 or r>=rows or c<0 or c>=cols or board[r][c]!=word[index] or visited[r][c]):
                return False
            visited[r][c]=True
            
            res = (backtrack(r+1,c,index+1) or
                   backtrack(r-1,c,index+1) or
                   backtrack(r,c+1,index+1) or
                   backtrack(r,c-1,index+1))
            visited[r][c]=False
            return res
        for r in range(rows):
            for c in range(cols):
                if backtrack(r,c,0):
                    return True
        return False
                
                    
                    
            
