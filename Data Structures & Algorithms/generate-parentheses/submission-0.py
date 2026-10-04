class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        res = []
        
        def dfs(open, close, sol):
            if close > open:
                return
            if open == n and close == n:
                res.append("".join(sol))
            if open > n or close > n:
                return
            sol.append("(")
            dfs(open + 1 , close, sol)
            sol.pop()
            sol.append(")")
            dfs(open, close + 1, sol)
            sol.pop()

        dfs(0, 0, [])

        return res
            
        
        