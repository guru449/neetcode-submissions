class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:

        res = []

        hs = set()

        def dfs(i, temp):
            if tuple(sorted(temp)) not in hs:
                hs.add(tuple(sorted(temp.copy())))
                res.append(temp.copy())
            if i >= len(nums):
                return
            temp.append(nums[i])
            dfs(i+1, temp)
            temp.pop()
            dfs(i+1, temp)



        dfs(0, [])

        return res

        