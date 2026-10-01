class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        stack = []
        maxArea = 0
        for (i,h) in enumerate(heights):
            start = i
            while stack and stack[-1][1] > h:
                idx, height = stack.pop()
                start = idx
                maxArea = max(maxArea, height * (i - idx))
            stack.append((start, h))

        while stack:
            idx, val = stack.pop()
            maxArea = max(maxArea, val * (len(heights) - idx))

        return maxArea