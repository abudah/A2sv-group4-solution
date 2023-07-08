class Solution:
    def findCenter(self, edges: List[List[int]]) -> int:
        graph = defaultdict(list)

        for source, destination in edges:
            graph[source].append(destination)
            graph[destination].append(source)

        for key, val in graph.items():
            if len(val) == len(graph) -1:
                return key            