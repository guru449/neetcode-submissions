class Solution:
    def hammingWeight(self, n: int) -> int:
        res  = 0
        while n > 0:
            print(n)
            if n & 1 == 1:
                res += 1
            n = n // 2
        
        return res

        # 1101
        # 0001

        # 0101
        # 0001