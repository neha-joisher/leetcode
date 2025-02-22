class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        rows,cols=len(board), len(board[0])
        path=set()
        
        def dfs(r,c,i):

            #termination condition
            if (i==len(word)):
                return True

           #if word[i] not found, then return False- Skip
            if (r<0 or c<0 or r>=rows or c>=cols or word[i]!=board[r][c] or (r,c) in path):
                return False

            #if word[i] found, then traverse in all for direction
            path.add((r,c))
            res= dfs(r,c+1,i+1) or dfs(r,c-1,i+1) or dfs(r+1,c,i+1) or dfs(r-1,c,i+1)
            path.remove((r,c))
            return res
        
        for r in range(rows):
            for c in range(cols):
                if dfs(r,c,0)==True: return True
        return False
        