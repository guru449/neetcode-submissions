class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        result = []
        total = len(nums)
        temp = []
        def dfs(i, temp, t):
            if t == target:
                result.append(temp.copy())
                return
            if t > target or i >= total:
                return
            temp.append(nums[i])
            dfs(i, temp, t + nums[i])
            temp.pop()
            dfs(i+1, temp, t)

        
        dfs(0, [], 0)


        return result
            
# Did on own ecvxcept tuple and hash thingy
# in a set you cant add a list because its mutable - it needs to be converted eto a tauple

# in a list of lists you cant add tuple, you need to convrert int back to list
        