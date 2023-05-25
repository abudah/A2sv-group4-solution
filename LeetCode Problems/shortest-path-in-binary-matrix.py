class Solution:
    def shortestPathBinaryMatrix(self, grid: List[List[int]]) -> int:
        directions =[[1,1],[-1,1],[1,-1],[-1,-1], [0,1], [1,0], [-1,0],[0,1],[0,-1]]
        queue = deque([(1, [0,0])])
  
        n = len(grid)
        visited = set()
        if grid[0][0] == 1:
            return -1
        def inbound(r,c):
            if r >= 0 and r < n and c >= 0 and c < n:
                return True
            return False
        while queue:
            count , pos = queue.popleft()
            if pos == [n-1,n-1]:
                return count
            for dr, dc in directions:
                r = pos[0] + dr
                c = pos[1] + dc
                if inbound(r, c) and grid[r][c] == 0:
                    grid[r][c] = 1
                    queue.append([count+1, [r, c]])
        return -1