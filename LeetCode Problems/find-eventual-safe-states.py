class Solution:
    def eventualSafeNodes(self, graph: List[List[int]]) -> List[int]:
        modified_graph = defaultdict(list)
        indegree = [0]*len(graph)

        for ind, val in enumerate(graph):
            for el in val:
                modified_graph[el].append(ind)
                indegree[ind] += 1
        queue = deque([])
        for i in range(len(graph)):
            if indegree[i] == 0:
                queue.append(i)

        res = []
        while queue:
            node = queue.popleft()
            res.append(node)
            for neigh in modified_graph[node]:
                indegree[neigh] -= 1
                if indegree[neigh] == 0:
                    queue.append(neigh)
        res.sort()
        return res
        