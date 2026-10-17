class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        
        # iterate each point
        # calculate the distance and store in heap with negative value as the heap is min heap by default along with the point
        # pop k elements from the heap based on distance and put it to final result
        heap = []
        for point in points:
            x, y = point
            distance = math.sqrt(pow(x,2) + pow(y,2))
            heapq.heappush(heap, (distance, point))
        result = []
        while heap and k > 0:
            distance , point = heapq.heappop(heap)
            result.append(point)
            k -= 1
        
        return result

        

        