from collections import defaultdict
class Solution:
    def validPath(self, n: int, edges: List[List[int]], source: int, destination: int) -> bool:
        

        graph = defaultdict(list)

        for vertices in edges:
            graph[vertices[0]].append(vertices[1])
            graph[vertices[1]].append(vertices[0])
        
        
        def bfs(graph, node):
            visited = set([node])
            queue = deque([node])

            while queue:
                node = queue.popleft()
                if node == destination:
                    return True

                for neighbours in graph[node]:
                    if neighbours not in visited:
                        visited.add(neighbours)
                        queue.append(neighbours)
            return False
        return bfs(graph, source)