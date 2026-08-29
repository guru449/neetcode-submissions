class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        result = []
        hs = set()
        total = len(nums)
        temp = []
        def dfs(i, temp, t):
            if t == target:
                sortedList = tuple(sorted(temp))
                if sortedList not in hs:
                    hs.add(sortedList)
                    result.append(list(sortedList))
                return
            if t > target or i >= total:
                return
            temp.append(nums[i])
            dfs(i, temp, t + nums[i])
            dfs(i+1, temp, t + nums[i])
            temp.pop()
            dfs(i+1, temp, t)

        
        dfs(0, [], 0)


        return result
            


        