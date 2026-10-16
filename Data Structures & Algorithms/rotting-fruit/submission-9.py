class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:

        queue = deque()

        m = len(grid)
        n = len(grid[0])

        dir = [[1,0], [0, 1], [-1,0], [0,-1]]

        visit = set()

        def rotOranges(i,j):
            for d in dir:
                a = i + d[0]
                b = j + d[1]
                if a < m and b < n and a >= 0 and b >= 0 and (a,b) not in visit and grid[a][b] == 1:
                    visit.add((a,b))
                    queue.append((a,b))
                    grid[a][b] = 2

        oranges = 0
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] == 2:
                    visit.add((i,j))
                    queue.append((i,j))
                if grid[i][j] != 0:
                    oranges += 1

        if oranges == 0:
            return 0
            
        time = -1

        while queue:
            size = len(queue)
            print(queue)
            time += 1
            for i in range(size):
                a, b = queue.popleft()
                rotOranges(a,b)
    
        if oranges == len(visit):
            return time
        
        else:
            return -1
            

        