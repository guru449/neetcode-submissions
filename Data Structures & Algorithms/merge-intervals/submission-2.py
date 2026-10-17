class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        
        intervals.sort()
        res = []
        res.append(intervals[0])

        for i in range(1, len(intervals)):
            ivl1 = res[-1]
            ivl2 = intervals[i]

            if ivl1[1] >= ivl2[0]:
                res.pop()
                res.append([min(ivl1[0], ivl2[0]), max(ivl1[1], ivl2[1])])
            else:
                res.append(ivl2)
            
        return res




        