class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        ROWS = len(matrix)
        COLUMNS = len(matrix[0])
        top  = 0
        bot = ROWS - 1

        while top <= bot:
            row = (top + bot) // 2
            if target > matrix[row][-1]:
                top = row + 1
            elif target < matrix[row][0]:
                bot = row - 1
            else:
                break
        
        if not (top <= bot):
            return False
        
        print(top)
        
        row = (top + bot) // 2
        left = 0
        right = COLUMNS - 1

        while left <= right:
            rowMid = (left + right) // 2
            val = matrix[row][rowMid]
            if val < target:
                left = rowMid + 1
            elif val > target:
                right = rowMid - 1
            else:
                return True

        return False


        
        