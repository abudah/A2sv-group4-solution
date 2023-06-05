class Solution:
    def updateMatrix(self, mat: List[List[int]]) -> List[List[int]]:
        directions = [[0,1], [1,0], [0, -1], [-1, 0]]
                
            
            
        result = [[sys.maxsize]*len(mat[0]) for i in range(len(mat))]
        queue = deque()
        for r in range(len(mat)):
            for c in range(len(mat[0])):
                if mat[r][c] == 0:
                    queue.append([r,c, 0])
                    result[r][c] = 0
        visited = set()
        while queue:
            row, col, d = queue.popleft()
            if d == 0:
                visited.clear()
            print(row, col)
            for dr, dc in directions:
                row_change = row + dr
                col_change = col + dc
                if row_change < 0 or row_change > len(mat)-1 or  col_change < 0 or col_change == len(mat[0]) or mat[row_change][col_change] == 0:
                    continue
                if (row_change, col_change) in visited:
                    continue
                visited.add((row_change, col_change))
                
                queue.append([row_change, col_change, d +1])
                result[row_change][col_change] = min(result[row_change][col_change],d +1)

        return result
        
        
                
                   