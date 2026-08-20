class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        num = {}
        for i, n in enumerate(nums):
            if target - n in num:
                return [num[target-n], i]
            num[n] = i
        


