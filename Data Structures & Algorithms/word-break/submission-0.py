class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        hm = {}
        def dfs(i):
            if i in hm:
                return hm[i]
            if i == len(s):
                return True
            res = False
            for word in wordDict:
                if word == s[i: i + len(word)]:
                    res = res or dfs(i + len(word))
            hm[i]  = res
            return hm[i]

        return dfs(0)

        