class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        m = len(matrix)
        n = len(matrix[0])
        top = 0
        bottom = m
        left = 0
        right = n
        res = []

        while top < bottom and left < right:

            for i in range(left, right):
                res.append(matrix[top][i])
            top += 1
            if not top < bottom:
                break
            for j in range(top, bottom):
                res.append(matrix[j][right - 1])
            right -= 1
            
            if not left < right:
                break

            for i in range(right - 1, left - 1, -1):
                res.append(matrix[bottom - 1][i])
            bottom -= 1

            if not top < bottom:
                break
            for j in range(bottom - 1, top - 1, -1):
                res.append(matrix[j][left])
            left += 1

            if not left < right:
                break
        return res
            

            