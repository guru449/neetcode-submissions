class Solution:
    def trap(self, height: List[int]) -> int:
        l = 0
        r = len(height) - 1
        leftMax = 0
        rightMax = 0
        result = 0
        while l <= r:
            if leftMax < rightMax:
                res = max(leftMax - height[l], 0)
                leftMax = max(leftMax, height[l])
                l += 1
            else:
                res = max(rightMax - height[r], 0)
                rightMax = max(rightMax, height[r])
                r -= 1
            result += res
        
        return result

