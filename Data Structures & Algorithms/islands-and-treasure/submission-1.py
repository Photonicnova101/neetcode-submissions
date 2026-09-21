from collections import deque
class Solution:
    def islandsAndTreasure(self, grid: List[List[int]]) -> None:
        m = len(grid)
        n = len(grid[0])
        INF = 2147483647
        q = ((r,c) for r in range(m) for c in range(n) if grid[r][c]==0)
        q =deque(q)

        while q:
            r,c = q.popleft()
            directions = [[1,0],[-1,0],[0,1],[0,-1]]
            for dr,dc in directions:
                nr,nc = r+dr,c+dc
                if 0<=nr<m and 0<=nc<n and grid[nr][nc]==INF:
                    grid[nr][nc]=grid[r][c]+1
                    q.append((nr,nc))
