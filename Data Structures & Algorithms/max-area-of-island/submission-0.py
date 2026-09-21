class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        m = len(grid)
        n= len(grid[0])
        visit = set()
        def dfs(r,c):
            if (r<0 or c<0 or r>=m or c>=n or grid[r][c]==0 or (r,c) in visit):
                return 0

            visit.add((r,c))
            return (1+dfs(r+1,c)+dfs(r-1,c)+dfs(r,c-1)+dfs(r,c+1))
                
            
        maxarea =0  
        for x in range(m):
            for y in range(n):
                maxarea =max(maxarea,dfs(x,y))
        return maxarea


