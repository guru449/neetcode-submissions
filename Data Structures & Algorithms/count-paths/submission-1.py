class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        i = 0
        j = 0
        hm = {}
        def dfs(i, j):
            if i == m - 1 and j == n - 1:
                return 1
            if i > m - 1 or j > n - 1:
                return 0
            
            if (i,j) in hm:
                return hm[(i,j)]
            hm[(i,j)] = dfs(i+1, j) + dfs(i, j + 1)
            return hm[(i,j)]

        hm[(0,0)] = dfs(0,0)

        return hm[(0,0)]

