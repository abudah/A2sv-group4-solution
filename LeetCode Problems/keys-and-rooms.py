class Solution:
    def canVisitAllRooms(self, rooms: List[List[int]]) -> bool:
        queue = deque([0])
        visited = set([0])

        while queue:
            node = queue.popleft()
            visited.add(node)
            for keys in rooms[node]:
                if keys not in visited:
                    queue.append(keys)
        if len(visited)  == len(rooms):
            return True
        return False