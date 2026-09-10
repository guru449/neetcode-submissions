class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:\

        left = 1

        right = max(piles)

        result = float("inf")

        mid = 0
        while left <= right:
            mid = (right + left) // 2
            counter = 0
            for p in piles:
                counter += math.ceil(p / mid)
                if counter > h:
                    break
            if counter > h:
                left = mid + 1
                continue
            right = mid - 1
            result = min(result, mid)

        return result
        