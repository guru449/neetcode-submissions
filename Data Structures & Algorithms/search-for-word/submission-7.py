class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        
        m = len(board)
        n = len(board[0])
        visit = set()
        def dfs(i, j, k):
            if i == len(word):
                return True
            if j< 0 or j >= m or k < 0 or k>= n or word[i] != board[j][k] or (j,k) in visit:
                return False

            visit.add((j,k))
            res = dfs(i + 1, j , k+1) or dfs(i + 1, j , k-1) or dfs(i + 1, j + 1, k) or  dfs(i + 1, j  - 1, k)
            visit.remove((j,k))
            return res
        

        for a in range(m):
            for b in range(n):
                if board[a][b] == word[0]:
                    visit = set()
                    if dfs(0, a, b):
                        
                        return True
        return False
                

