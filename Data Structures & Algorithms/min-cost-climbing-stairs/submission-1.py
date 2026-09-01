class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        
        n  = len(cost)
        hm = {}
        def dfs(i):
            if i == n:
                return 0
            if i > n:
                return float('inf')
            if i in hm:
                return hm[i]
            hm[i] = cost[i] + min(dfs(i+1), dfs(i+2))
            return hm[i]

        return min(dfs(0), dfs(1))