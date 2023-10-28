n, m = map(int, input().split())
grid = []

for row in range(n):
    cols = [i for i in input()]
    grid.append(cols)

visited = set()

directions = [[0, 1], [1,0], [-1, 0], [0, -1]]

def inbound(r, c):
    return r >= 0 and r < n and c >= 0 and c < m

def dfs(r, c):
    if (r, c) in visited:
        return
    visited.add((r, c))
    
    for dr, dc in directions:
        row = dr + r
        col = dc + c
        if inbound(row, col) and grid[row][col] == ".":
            if (row, col) in visited:
                continue
            dfs(row, col)
count = 0 
for r in range(n):
    for c in range(m):
        if (r, c) in visited:
            continue
        if grid[r][c] == ".":
            count += 1
            dfs(r, c)
            
print(count)