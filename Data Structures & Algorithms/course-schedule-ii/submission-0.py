class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        adjGraph = {i:[] for i in range(numCourses) }

        for src, des in prerequisites:
            adjGraph[src].append(des)
        
        res = []
        hs = set()
        cycle = set()
        def dfs(crs):
            if crs in hs:
                return True
            if crs in cycle:
                return False
            cycle.add(crs)
            for course in adjGraph[crs]:
                if dfs(course) == False:
                    return False
            hs.add(crs)
            res.append(crs)

            return True


        for i in range(numCourses):
            if not dfs(i):
                return []
        
        return res




        