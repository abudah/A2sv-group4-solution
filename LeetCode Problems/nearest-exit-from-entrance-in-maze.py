class Solution:
    def nearestExit(self, maze: List[List[str]], entrance: List[int]) -> int:
        queue = deque([])
        directions = [[0, 1], [1,0], [0,-1], [-1, 0]]

        queue.append([0, entrance])
        def outbound(r, c):
            return r < 0 or r >= len(maze) or c < 0 or c >= len(maze[0])
        visited = set()
        while queue:
            dist, pos = queue.popleft()
            if (pos[0], pos[1]) in visited:
                continue
            visited.add((pos[0], pos[1]))
            for dr, dc in directions:
                row = pos[0] + dr
                col = pos[1] + dc

                if outbound(row, col):
                    if pos != entrance:
                        return dist
                elif maze[row][col] == ".":
                    queue.append([dist + 1, [row,col]])
        return -1