class Solution:
    def findMin(self, nums: List[int]) -> int:

        left = 0
        right = len(nums) - 1
        nums = nums  + nums
        def dfs(left, right):
            if left > right:
                return float("inf")
            mid = (left + right) // 2
            print(mid)
            if mid + 1 < len(nums) and nums[mid] > nums[mid + 1]:
                return nums[mid+1]
            else:
                return min(dfs(mid + 1, right),dfs(left, mid - 1))
        
        result = dfs(left, right)
        
        if result == float("inf"):
            return min(nums[0], nums[len(nums) - 1])
        else:
            return result


            



