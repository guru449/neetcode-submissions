class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        hm = collections.defaultdict(int)
        hm[0] = 1
        curSum = 0
        res = 0
        for n in nums:
            curSum += n
            if curSum - k in hm:
                res = res + hm[curSum - k]
            hm[curSum] += 1
        
        return res


        