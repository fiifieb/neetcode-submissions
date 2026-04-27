class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        max_area = 0
        visited = set()

        def dfs(x,y):
            directions = [(0,1),(1,0),(-1,0),(0,-1)]
            area = 1
            for dx, dy in directions:
                if 0<=dx+x<len(grid) and 0<=dy+y<len(grid[0]) and grid[x+dx][y+dy]==1:
                    if (x+dx,y+dy) not in visited:
                        visited.add((x+dx,y+dy))
                        area += dfs(x+dx,y+dy)

            return area


        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j]==1:
                    if (i,j) not in visited:
                        visited.add((i,j))
                        max_area = max(max_area,dfs(i,j))


        return max_area