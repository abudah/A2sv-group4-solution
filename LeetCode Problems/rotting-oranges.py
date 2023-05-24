class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        directions =[[0,1],[1,0], [-1,0], [0,-1]]
        queue = deque()

        time, fresh = 0, 0
        for row in range(len(grid)):
            for col in range(len(grid[0])):
                if grid[row][col] == 1:
                    fresh += 1
                if grid[row][col] == 2:
                    queue.append([row, col])
        
        while queue and fresh > 0:
            for _ in range(len(queue)):
                r, c  = queue.popleft()
                for row_change, col_change in directions:
                    new_row = r + row_change
                    new_col = c + col_change
                    if new_row < 0 or new_row >= len(grid) or  new_col < 0 or new_col >= len(grid[0]) or grid[new_row][new_col] != 1:
                        continue
                    grid[new_row][new_col] = 2
                    queue.append([new_row, new_col])
                    fresh -= 1
            time += 1

        return time if fresh == 0 else -1

