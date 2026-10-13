class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        finalResult = []
        hs = set()
        def twoSum(j, target) -> List: 
            hm = {}
            res = []
            for i in range(j, len(nums)):
                if target - nums[i] in hm:
                    res.append([nums[i], target - nums[i]])
                hm[nums[i]] = i
            return res

        for i in range(len(nums) - 3 + 1):
            res = twoSum(i + 1, -1 * nums[i])
            for r in res:
                if len(r) == 2:
                    r.append(nums[i])
                    if tuple(sorted(r)) not in hs:
                        finalResult.append(r)
                        hs.add(tuple(sorted(r)))



        return finalResult
            

