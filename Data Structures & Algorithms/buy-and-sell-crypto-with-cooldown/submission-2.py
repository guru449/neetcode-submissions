class Solution:
    def maxProfit(self, prices: List[int]) -> int:

        hm = {}

        def dfs(i, buy):
            if (i,buy) in hm:
                return hm[(i,buy)]
            if i >= len(prices):
                return 0

            if buy:
                buying = dfs(i+1, not buy) - prices[i]
                cooldown1 = dfs(i+1, buy)
                hm[(i, buy)] = max(buying, cooldown1)

            else:
                selling = prices[i] + dfs(i+2, not buy)
                cooldown2 = dfs(i+1, buy)
                hm[(i, buy)] = max(selling, cooldown2)
            return hm[(i,buy)]

        return dfs(0,True)


            
            


            
        