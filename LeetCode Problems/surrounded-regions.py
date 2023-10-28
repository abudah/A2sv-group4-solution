class Solution:
    def solve(self, board: List[List[str]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        max_col = len(board[0])
        max_row = len(board)

        queue = deque([])
        visited = set()
        for row in range(max_row):
            if board[row][0] == "O":
                queue.append((row, 0))
            if board[row][max_col - 1] == "O":
                queue.append((row, max_col - 1))
                

        for col in range(max_col):
            if board[0][col] == "O":
                queue.append((0, col))
            if board[max_row - 1][col] == "O":
                queue.append((max_row - 1, col))
        def inbound(r, c):
            return r >= 0 and r < max_row and c >= 0 and c < max_col
            
        directions = [[-1, 0], [0, -1], [1, 0], [0, 1]]

        while queue:
            r, c  = queue.popleft()
            if (r, c) in visited:
                continue
            visited.add((r, c))
            for dr, dc in directions:
                row = r + dr
                col = c +dc
                if inbound(row, col) and board[row][col] == "O":
                    if (row, col) in visited:
                        continue
                    queue.append((row, col))
        for row in range(max_row):
            for col in range(max_col):
                if (row, col)  in visited:
                    continue
                board[row][col] ="X"



