class Solution:
    def wallsAndGates(self, rooms: List[List[int]]) -> None:
        """
        Do not return anything, modify rooms in-place instead.
        """
        rows=len(rooms)
        cols=len(rooms[0])
        visited=set()
        queue=collections.deque()

        def addCell(r,c):
            if r<0 or r>=rows or c<0 or c>=cols or (r,c) in visited or rooms[r][c]==-1:
                return 

            visited.add((r,c))
            queue.append([r, c])

        for r in range(rows):
            for c in range(cols):
                if rooms[r][c]==0:
                    queue.append([r,c])
                    visited.add((r,c))
        
        dist=0
        while queue:
            for i in range(len(queue)):
                r,c=queue.popleft()
                rooms[r][c]=dist
                addCell(r+1,c)
                addCell(r-1,c)
                addCell(r,c-1)
                addCell(r,c+1)
            dist+=1
