class Solution:
    def islandsAndTreasure(self, grid: List[List[int]]) -> None:
    
        m = len(grid)
        n = len(grid[0])
        
        q = deque()

        visit = set()

        def addRoom(i, j):
            if i < 0 or i >= m or j < 0 or j >= n or grid[i][j] == -1 or (i,j) in visit:
                return
            else:
                q.append([i,j])
                visit.add((i,j))
            
        for i in range(m):
            for j in range(n):
                if grid[i][j] == 0:
                    q.append([i,j])
                    visit.add((i,j))
        dist = 0

        while q:
            for i in range(len(q)):
                a, b = q.popleft()
                grid[a][b] = dist
                addRoom(a + 1, b)
                addRoom(a, b+1)
                addRoom(a -1 , b)
                addRoom(a, b-1)
            dist += 1
        

                