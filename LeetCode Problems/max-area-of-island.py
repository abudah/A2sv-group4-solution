class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        res = 0
        area = 0
        directions = [(0, 1),(1, 0), (0, -1),(-1, 0)]

        def dfs(grid,row, col):
            nonlocal area
            if row < 0 or col < 0 or row >= len(grid) or col >= len(grid[0]) or grid[row][col] == 0:
                return
            
            area += 1
            grid[row][col] = 0
            for row_change, col_change in directions:
                dfs(grid, row + row_change, col + col_change)
            return 
        
        for row in range(len(grid)):
            for col in range(len(grid[0])):
                if grid[row][col] == 1:
                    area = 0
                    dfs(grid, row, col)
                    res = max(res, area)
        
        return res