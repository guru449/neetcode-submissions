class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        hm = collections.defaultdict(int)
        l = 0
        res = 0
        for r in range(len(s)):
            hm[s[r]] += 1
            if r - l + 1 - max(hm.values()) > k:
                hm[s[l]] -= 1
                l += 1

            res = max(res, r - l + 1)

        return res

  



        