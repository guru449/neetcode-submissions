class Solution:
    def isHappy(self, n: int) -> bool:
        
        def sumOfSquares(n):
            res = 0
            while n > 0:
                rem = n % 10
                n = n // 10
                res = res + rem*rem
            return res


        visit = set()

        while n not in visit:
            visit.add(n)
            n = sumOfSquares(n)
            if n == 1:
                return True
        
        return False



