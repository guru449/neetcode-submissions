class Solution:
    def minWindow(self, s: str, t: str) -> str:
        l = r = 0
        hm = collections.Counter(t)
        h = {}
        have = 0
        need = len(hm)
        res = float("inf")
        resultString = ""
        while r < len(s):
            if s[r] in hm:
                h[s[r]] = h.get(s[r], 0) +  1
            if s[r] in hm and h[s[r]] == hm[s[r]]:
                have += 1
            while have == need:
                if r - l + 1 < res:
                    res = r - l + 1
                    resultString = s[l:r + 1]
                if s[l] in h:
                    h[s[l]] -= 1
                if s[l] in h and h[s[l]] < hm[s[l]]:
                    have -= 1
                l += 1

            r += 1
        return resultString
                