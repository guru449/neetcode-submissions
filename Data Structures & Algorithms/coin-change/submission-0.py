class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:

        hm = {}
        def dfs(i, val):
            if (i,val) in hm:
                return hm[(i,val)]
            if i >= len(coins) or val > amount:
                return float("inf")
            if val == amount:
                return 0
            
            hm[(i,val)] = min(1 + dfs(i+1, val + coins[i]), 
             1 + dfs(i, val + coins[i]),
              dfs(i+1, val))
            
            return hm[(i,val)]
        
        result = dfs(0, 0)
        if result == float("inf"):
            return -1
        else:
            return result
        
        