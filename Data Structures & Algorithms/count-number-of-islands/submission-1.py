class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        visited = set()
        islands = 0        

        def dfs(x,y):
            directions = [(1,0),(0,1),(-1,0),(0,-1)]
            for dx,dy in directions:
                if 0<=x+dx<len(grid) and 0<=y+dy<len(grid[0]):
                    if (x+dx,y+dy) not in visited and grid[x+dx][y+dy]=='1':
                        visited.add((x+dx,y+dy))
                        dfs(x+dx,y+dy)


        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] == '1':
                    if (i,j) not in visited:
                        visited.add((i,j))
                        dfs(i,j)
                        islands += 1

        return islands