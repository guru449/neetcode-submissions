class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        preMap = {i: [] for i in range(numCourses)}
        
        for src, des in prerequisites:
            preMap[src].append(des)
        
        visit = set()

        def dfs(crsMain):
            print(crsMain)
            for crs in preMap[crsMain]:
                if preMap[crs] == []:
                    continue
                if crs in visit:
                    return False
                visit.add(crs)
                if not dfs(crs):
                    return False
                visit.remove(crs)
                preMap[crs] = []
            
            return True
                

        for crs in range(numCourses):
            visit = set()
            res = dfs(crs)
            if not res:
                return False
        return True
        