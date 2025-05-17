class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:

        count_Fresh_Fruit=0
        rows = len(grid)
        cols=len(grid[0])
        queue=collections.deque()

        def addFruit(r,c):
            nonlocal count_Fresh_Fruit
            if r<0 or r>=rows or c<0 or c>=cols or grid[r][c] != 1:
                return
            grid[r][c]=2
            queue.append([r,c])
            count_Fresh_Fruit-=1

        for r in range(rows):
            for c in range(cols):
                if grid[r][c]==1:
                    count_Fresh_Fruit+=1
                if grid[r][c]==2:
                    queue.append([r,c])

        print(count_Fresh_Fruit)

        time=0
        while queue and count_Fresh_Fruit > 0:
            for i in range(len(queue)):
                r,c=queue.popleft()
                addFruit(r+1,c)
                addFruit(r-1,c)
                addFruit(r,c+1)
                addFruit(r,c-1)
            time+=1
        if len(queue)==0 and count_Fresh_Fruit>0:
            return -1
        return time
        