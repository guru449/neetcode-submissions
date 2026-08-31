class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        row = len(grid)
        col = len(grid[0])
        visit = set()
        directions = [[1, 0],[0,1],[-1,0],[0,-1]]
        result = 0
        
        def bfs(i, j):
            q = collections.deque()
            q.append((i,j))
            visit.add((i,j))
            while len(q) > 0:
                ni, nj = q.popleft()
                for dr, dc in directions:
                    r = dr + ni
                    c = dc + nj
                    if r  >= 0 and r < row and c >= 0 and c < col and grid[r][c] == "1" and (r,c) not in visit:
                        visit.add((r,c))
                        q.append((r,c))
            
                    
        for i in range(row):
            for j in range(col):
                if grid[i][j] == "1" and (i,j) not in visit:
                    bfs(i, j)
                    result += 1
        return result
        


        