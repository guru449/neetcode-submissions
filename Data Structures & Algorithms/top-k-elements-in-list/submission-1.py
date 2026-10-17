class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        hm = {}
        heap = []

        for n in nums:
            hm[n] = hm.get(n, 0) + 1
        
        for kk,v in hm.items():
            heapq.heappush(heap, (-v, kk))
        
        res = []

        while k > 0:
            v, key = heapq.heappop(heap)
            res.append(key)
            k -= 1
        
        return res

        