class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        hm = collections.defaultdict(int)

        l = r  = 0
        res = 0

        while r < len(s):
            if s[r] not in hm:
                hm[s[r]] = 1
            else:
                hm[s[r]] = hm[s[r]] + 1
                while l < r:
                    hm[s[l]] = hm[s[l]] - 1
                    if hm[s[l]] == 0:
                        del hm[s[l]]
                    if s[r] == s[l]:
                        l += 1
                        break
                    l += 1
                    

            res = max(res, r - l + 1)
            r += 1
        
        return res
        