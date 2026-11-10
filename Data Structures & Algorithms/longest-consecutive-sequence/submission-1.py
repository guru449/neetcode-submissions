class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        hs = set(nums)
        result = 0
        for n in nums:
            length = 0
            if (n-1) not in hs:
                while n + length in hs:
                    length += 1
            result = max(result, length)

        return result
