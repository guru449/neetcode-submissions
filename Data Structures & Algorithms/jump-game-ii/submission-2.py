class Solution:
    def jump(self, nums: List[int]) -> int:
        res = float("inf")
        hm = {}
        def dfs(i):
            if i in hm:
                return hm[i]
            nonlocal res
            if i >= len(nums) - 1:
                return 0
            best = float("inf")
            for j in range(1, nums[i] + 1):
                best = min(best, 1 + dfs(i + j))
            hm[i] = best
            return hm[i]

        return dfs(0)


        