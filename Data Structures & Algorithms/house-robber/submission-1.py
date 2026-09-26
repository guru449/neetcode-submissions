class Solution:
    def rob(self, nums: List[int]) -> int:

        hm = collections.defaultdict(int)

        def dfs(i):
            if i in hm:
                return hm[i]
            if i >=  len(nums):
                return 0

            hm[i] = max(nums[i] + dfs(i+2) , dfs(i+1))
            return hm[i]
        


        return dfs(0)

        