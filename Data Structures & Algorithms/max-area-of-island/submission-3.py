class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        rows = len(grid)
        cols = len(grid[0])
        visit = set()
        def dfs(i,j):
            if (i,j) in visit or i not in range(rows) or j not in range(cols) or grid[i][j] == 0:
                return 0
            visit.add((i,j))
            return 1 + (dfs(i+1, j) +  dfs(i, j+1) + dfs(i-1, j) +  dfs(i, j-1))
            
        result = 0
        for i in range(rows):
            for j in range(cols):
                if grid[i][j] == 1 and (i,j) not in visit:
                    result = max(result, dfs(i,j))
        return result        