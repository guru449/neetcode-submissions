class Solution:
    def canJump(self, nums: List[int]) -> bool:
        hm = {}
        
        def dfs(i):
            if i >= len(nums) - 1:
                return True
            if i in hm:
                return hm[i]
            hm[i]  = False
            for j in range(i + 1, i + nums[i] + 1):
                if dfs(j):
                    hm[i] = True
                    break
            return hm[i]

        return dfs(0)

        