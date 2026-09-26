class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        #store the points and the value of sq lenth
        #pop k elements
        # put to result 
        #return

        res = []
        heap = []

        for p in points:
            p1, p2 = p
            val = math.sqrt(pow(p1, 2) + pow(p2, 2))
            heapq.heappush(heap, [val, p])

        while k > 0:
            val, p = heapq.heappop(heap)
            p1, p2 = p
            k -= 1     
            res.append([p1,p2])

        return res     


        