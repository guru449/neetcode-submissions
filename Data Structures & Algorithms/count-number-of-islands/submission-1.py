class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:

        visit = set()
        m = len(grid)
        n = len(grid[0])
        def dfs(i ,j):
            if (i,j) in visit:
                return
            if i < 0 or i >= m or j < 0 or j >= n:
                return
            if grid[i][j] == "0":
                return
            else:
                visit.add((i,j))
            dfs(i+1, j)
            dfs(i, j+1)
            dfs(i - 1, j)
            dfs(i, j - 1)
        count = 0
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] == "1" and (i,j) not in visit:
                    dfs(i,j)
                    count += 1
        
        return count

            

        