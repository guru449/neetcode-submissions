class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        prefixProduct = [1] * len(nums)
        postProduct = [1] * len(nums)
        res = [1] * len(nums)
        for i in range(1, len(nums)):
            prefixProduct[i] = nums[i-1] * prefixProduct[i-1]

        for i in range(len(nums)-2, -1, -1):
            postProduct[i] = nums[i+1] * postProduct[i+1]
        
        for i in range(len(prefixProduct)):
            res[i] = prefixProduct[i] * postProduct[i]
        
        return res



        