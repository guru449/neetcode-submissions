class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        count = collections.Counter(nums)
        heap = []
        heapq.heapify(heap)
        res = []
        for c, v in count.items():
            heapq.heappush(heap, (-v, c)) 
        
        while k > 0:
            count, value = heapq.heappop(heap)
            res.append(value)
            k -= 1
    
        return res
