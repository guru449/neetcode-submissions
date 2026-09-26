class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        heap = []
        res = float("inf")
        for n in nums:
            heapq.heappush(heap, -n)
        
        while k > 0:
            val = heapq.heappop(heap)
            k -= 1
            res = min(res,-val)

        return res
        