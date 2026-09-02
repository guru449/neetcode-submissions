class Solution:
    def canJump(self, nums: List[int]) -> bool:

        hm = {}
        
        n = len(nums)
        def dfs(i):
            if i == n - 1: 
                return True
            if i in hm:
                return hm[i]
            
            if i >= n:
                return False
            for j in range(i + 1 , i + 1 +  nums[i]):
                if dfs(j):
                    hm[i] = True
                    return hm[i]
            hm[i] = False
            return hm[i]
        
        return dfs(0)



        