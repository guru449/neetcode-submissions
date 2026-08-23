class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        hs = set()
        result = 0
        l = r = 0
        while r < len(s):
            while s[r] in hs and l <= r:
                hs.remove(s[l])
                l += 1
            hs.add(s[r])
            r += 1
            result = max(result, len(hs))

        return result

