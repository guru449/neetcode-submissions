class Solution:
    def countBits(self, n: int) -> List[int]:

        res = []
        for i in range(n+1):
            val = i
            count = 0
            while val > 0:
                if val % 2 == 1:
                    count += 1
                val = val // 2
            
            res.append(count)
        
        return res
                

        