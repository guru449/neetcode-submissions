class Solution:
    def change(self, amount: int, coins: List[int]) -> int:

        hm = {}

        def dfs(i, val):
            if (i,val) in hm:
                return hm[(i,val)]
            if i >= len(coins):
                return 0
            if val > amount:
                return 0
            if val == amount:
                return 1

            hm[(i,val)] =  dfs(i, val + coins[i]) + dfs(i+1, val)
            return hm[(i,val)]
        
        return dfs(0, 0)

        