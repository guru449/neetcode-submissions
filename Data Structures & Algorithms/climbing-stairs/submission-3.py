class Solution:
    def climbStairs(self, n: int) -> int:
        hm = { 0: 0, 1: 1, 2:2}
        def dfs(i):
            if i == 0:
                return 1
            if i < 0:
                return 0
            if i in hm:
                return hm[i]
            hm[i] = dfs(i-1) + dfs(i - 2)
            return hm[i]

        dfs(n)

        return hm[n]