class Solution:
    def maxProbability(self, n: int, edges: List[List[int]], succProb: List[float], start_node: int, end_node: int) -> float:
        distances= [-1e9]*n
        distances[start_node] = 1
        
        queue = deque([])
        queue.append(start_node)
        graph = defaultdict(list)
        for i in range(len(edges)):
            graph[edges[i][0]].append([edges[i][1], succProb[i]])
            graph[edges[i][1]].append([edges[i][0], succProb[i]])

        while queue:
            node = queue.popleft()
            for neigh in graph[node]:
                if distances[node] * neigh[1] > distances[neigh[0]]:
                    distances[neigh[0]] = distances[node] * neigh[1]
                    queue.append(neigh[0])

        if distances[end_node] != -1e9:
            return distances[end_node]
        return 0.0