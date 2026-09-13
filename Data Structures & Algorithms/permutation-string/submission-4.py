class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        
        if len(s1) > len(s2):
            return False
        hm1 = collections.defaultdict(int)

        for s in s1:
            hm1[s] += 1

        hm2 = collections.defaultdict(int)

        l = 0
        r = len(s1)

        for i in range(len(s1)):
            hm2[s2[i]] += 1
        
        if hm1 == hm2:
            return True
        
        while r < len(s2):
            hm2[s2[r]] += 1
            hm2[s2[l]] -= 1
            if hm2[s2[l]] == 0:
                del hm2[s2[l]]
            if hm1 == hm2:
                return True
            r += 1
            l += 1
        return False







        
        