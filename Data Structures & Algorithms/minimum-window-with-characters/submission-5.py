class Solution:
    def minWindow(self, s: str, t: str) -> str:
        thm = collections.Counter(t)
        shm = collections.defaultdict(int)
        have = 0
        need = len(thm)
        l = 0 
        r = 0
        res = ""
        maxLength = float("inf")
        while r < len(s) and l <= r:
            shm[s[r]] += 1
            if s[r] in thm and shm[s[r]] == thm[s[r]]:
                have += 1

            while have == need:
                if r + 1 - l < maxLength:
                    maxLength = r + 1 - l
                    res = s[l:r+1]
                shm[s[l]] -= 1
                if s[l] in thm and shm[s[l]] < thm[s[l]]:
                    have -= 1
                l += 1
            r += 1

        return res

        