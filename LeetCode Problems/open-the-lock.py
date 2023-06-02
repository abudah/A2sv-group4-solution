class Solution:
    def openLock(self, deadends: List[str], target: str) -> int:
        def moves(lock):
            possiblities = []
            for i in range(4):
                move = str((int(lock[i]) + 1)%10)
                possiblities.append(lock[:i] + move + lock[i+1:])
                move = str((int(lock[i]) - 1)%10)
                possiblities.append(lock[:i] + move + lock[i+1:])
            return possiblities

        if "0000" in deadends:
            return -1
        
        queue = deque()
        queue.append(['0000', 0])

        visited = set(deadends)
        visited.add('0000')

        while queue:
            lock, turns = queue.popleft()
            if lock == target:
                return turns
            for state in moves(lock):
                if state not in visited:
                    print(state)
                    queue.append([state, turns + 1])
                    visited.add(state)
        return -1