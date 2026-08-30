class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        maxHeap = []
        
        for s in stones:
            heapq.heappush(maxHeap, s * -1)
        heapq.heapify(maxHeap)

        while len(maxHeap) > 1:
            stone1 = heapq.heappop(maxHeap) * -1
            stone2 = heapq.heappop(maxHeap) * -1
            stone3 = (stone1 - stone2) * -1
            heapq.heappush(maxHeap,stone3)

        if len(maxHeap) == 1:
            return maxHeap[0] * -1
        else:
            return 0



        