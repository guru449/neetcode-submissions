class Solution:
    def rob(self, nums: List[int]) -> int:
        if len(nums) == 1:
            return nums[0]
        hm1 = {}
        def dfs1(i):
            if i in hm1:
                return hm1[i]
            if i >= len(nums):
                return 0
            hm1[i] = max(dfs1(i+1), nums[i] + dfs1(i+2))
            return hm1[i]

        hm2 = {}

        def dfs2(i):
            if i in hm2:
                return hm2[i]
            if i >= len(nums) - 1:
                return 0
            hm2[i] = max(dfs2(i+1), nums[i] + dfs2(i+2))
            return hm2[i]

    

    
        return max(dfs2(0), dfs1(1))
        