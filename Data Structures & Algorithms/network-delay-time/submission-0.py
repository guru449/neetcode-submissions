class Solution:
    def networkDelayTime(self, times: List[List[int]], n: int, k: int) -> int:
        edges = collections.defaultdict(list)

        for n1, n2, v in times:
            edges[n1].append([n2,v])
        

        minHeap = [[0,k]]

        visit = set()

        t = 0

        while len(minHeap) > 0:
            nw, nv = heapq.heappop(minHeap)
            if nv in visit:
                continue
            visit.add(nv)
            t  = max(t, nw)
            for node, weight in edges[nv]:
                if node in visit:
                    continue
                heapq.heappush(minHeap, [nw + weight, node])
        
        return t if len(visit) == n else -1

