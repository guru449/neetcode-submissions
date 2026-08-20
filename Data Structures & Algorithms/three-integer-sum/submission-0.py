class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        result = []

        for i in range(len(nums)):
            hs = set()
            for j in range(i+1, len(nums)):
                needed = -nums[i] - nums[j]
                triplet = [needed, nums[i], nums[j]]
                triplet.sort()
                if needed in hs and triplet not in result:
                    result.append(triplet)
                hs.add(nums[j])
        
        return  result

        