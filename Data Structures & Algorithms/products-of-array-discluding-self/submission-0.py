class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        prefix = 1
        res = [0] * len(nums)
        for i in range(len(nums)):
            res[i] = prefix
            prefix = nums[i] * prefix
        
        postfix = 1
        for i in range(len(nums) -1 , -1, -1):
            res[i] = res[i] * postfix
            postfix = postfix * nums[i]
        
        return res



        