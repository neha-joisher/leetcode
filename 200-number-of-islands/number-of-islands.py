class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        rows=len(grid)
        cols=len(grid[0])
        visited=set()
        countOfIslands=0

        def dfs(r,c):
            if r<0 or c<0 or r>=rows or c>=cols or grid[r][c]=="0" or (r,c) in visited:
                return
            #condition to return count as 1 and mark as visited
            

            visited.add((r,c))

            #traverse in all four directions
            dfs(r+1,c) or dfs(r-1,c) or dfs(r,c+1) or dfs(r,c-1)
        
        
        for r in range(rows):
            for c in range(cols):
                if grid[r][c]=="1" and (r,c) not in visited:
                    dfs(r,c)
                    countOfIslands+=1
        return countOfIslands
        