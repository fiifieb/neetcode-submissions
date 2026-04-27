class Solution:
    def islandsAndTreasure(self, grid: List[List[int]]) -> None:
        row = len(grid) #4
        col = len(grid[0])#4
        def bfs(r,c): #0,0
            distance = 0 #2
            q = deque() 
            q.append((r,c))
            dirs = [(1,0), (0,1), (-1,0), (0,-1)]
            visited = set() #{(0,0), (1,0), (2,0)}

            while q: #[(2,0), (1,1)]
                distance += 1
                length = len(q) #2
                for _ in range(length):
                    x, y = q.popleft() #2,0
                    visited.add((x,y))
                    for dx, dy in dirs: #3,0
                        dx, dy = x+dx, y+dy
                        if 0<=dx<row and 0<=dy<col:
                            if grid[dx][dy] == -1 or (dx,dy) in visited:
                                continue
                            if grid[dx][dy] > 0:
                                q.append((dx, dy))
                            else:
                                distance += grid[dx][dy]
                                grid[r][c] = distance
                                return 
                

        
        for i in range(row):
            for j in range(col): #0, 0
                if grid[i][j] == 2147483647:
                    bfs(i,j)