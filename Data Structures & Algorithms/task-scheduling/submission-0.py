class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        
        hm = Counter(tasks)

        heap = [-v for v in hm.values()]
        heapq.heapify(heap)

        queue = deque()

        time = 0
        while heap or queue:
            time += 1
            if heap:
                value = heapq.heappop(heap)  + 1
                if value:
                    queue.append([value, time + n])

            if queue and queue[0][1] == time:
                b, t = queue.popleft()
                heapq.heappush(heap, b)

        return time