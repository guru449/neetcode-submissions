class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:

        queue = deque()

        m = len(grid)
        n = len(grid[0])

        dir = [[1,0], [0, 1], [-1,0], [0,-1]]

        fresh = 0

        def rotOranges(i,j):
            nonlocal fresh
            for d in dir:
                a = i + d[0]
                b = j + d[1]
                if a < m and b < n and a >= 0 and b >= 0 and grid[a][b] == 1:
                    queue.append((a,b))
                    grid[a][b] = 2
                    fresh -= 1

        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] == 2:
                    queue.append((i,j))
                if grid[i][j] == 1:
                    fresh += 1

        if fresh == 0:
            return 0

        time = -1

        while queue:
            size = len(queue)
            time += 1
            for i in range(size):
                a, b = queue.popleft()
                rotOranges(a,b)
    
        return  time if not fresh else  -1
            

        