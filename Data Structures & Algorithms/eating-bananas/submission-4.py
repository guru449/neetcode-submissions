class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        def canEat(rate):
            totalHours = 0
            for p in piles:
                totalHours += math.ceil((p / rate))
            if totalHours <= h:
                return True

        result = max(piles)

        l = 1
        r = max(piles)

        while l <= r:
            m = (r + l) // 2
            if canEat(m):
                result = min(result, m)
                r = m - 1
            else:
                l = m + 1
        
        return result
        