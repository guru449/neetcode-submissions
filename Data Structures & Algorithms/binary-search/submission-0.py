class Solution:
    def search(self, nums: List[int], target: int) -> int:
        l = 0
        r = len(nums) - 1

        while l <= r:
            med = (l + r) // 2
            print(med)
            if target < nums[med]:
                r = med - 1
            elif target > nums[med]:
                l = med + 1
            else:
                return med
        return -1
            