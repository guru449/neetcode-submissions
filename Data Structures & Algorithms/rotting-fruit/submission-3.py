class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:

        m = len(grid)
        n = len(grid[0])
        visit = set()
        q = deque()
        fresh = 0
        for i in range(m):
            for j in range(n):
                if grid[i][j] == 2:
                    q.append([i,j])
                    visit.add((i,j))
                if grid[i][j] == 1:
                    fresh += 1
        res = 0

        def addOrange(i,j):
            nonlocal fresh
            if i < 0 or j < 0 or i >= m or j >= n  or grid[i][j] == 0 or (i,j) in visit or grid[i][j] == 2:
                return
            else:
                q.append([i,j])
                visit.add((i,j))
                fresh -= 1
        
        while q and fresh > 0:
            for i in range(len(q)):
                a, b = q.popleft()
                
                addOrange(a+1,b)
                addOrange(a,b+1)
                addOrange(a-1,b)
                addOrange(a,b-1)
            
            res += 1
        
        if fresh == 0:
            return res
        else:
            return -1

        