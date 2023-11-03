class Solution:
    def shortestBridge(self, grid: List[List[int]]) -> int:
        one_island = set()
        queue = deque([])

        directions = [[0, 1], [1, 0], [-1, 0], [0, -1]]
        def inbound(r,c):
            return r >= 0 and r < len(grid) and c >= 0 and c < len(grid[0])
        def dfs(r,c):
            if (r, c) in one_island:
                return
            one_island.add((r,c))
            queue.append([0, [r, c]])
            for dr, dc in directions:
                row = r + dr
                col = c + dc
                if inbound(row, col) and grid[row][col] == 1:
                    dfs(row, col)
        for r in range(len(grid)):
            for c in range(len(grid[0])):
                if grid[r][c] == 1:
                    dfs(r, c)
                    break
            if one_island:
                break
                
        visited = set()
        while queue:
            dist, pos = queue.popleft()
            r, c = pos
            if (r, c) in visited:
                continue
            visited.add((r,c))
            for dr, dc in directions:
                row = r + dr
                col = c + dc

                if inbound(row,col) and grid[row][col] == 1:
                    if (row, col) not in one_island:
                        return dist
                elif inbound(row,col) and grid[row][col] == 0:
                    queue.append([dist + 1, [row,col]])
                    
                


