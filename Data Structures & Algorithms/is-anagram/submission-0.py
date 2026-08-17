class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        
        hm = {}

        for n in s:
            hm[n] = hm.get(n, 0) + 1
        
        for m in t:
            if m not in hm:
                return False
            hm[m] -= 1
            if hm[m] < 0:
                return False
        
        return True
        
        
        
    
        