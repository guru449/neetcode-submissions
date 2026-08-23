class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        l = r = 0
        result = 0
        while r < len(prices):
            result = max(result , prices[r] - prices[l])
            if prices[r] < prices[l]:
                l = r
            r += 1
        return result

    #didnt solve on own