class Solution:
    def findTheCity(self, n: int, edges: List[List[int]], distanceThreshold: int) -> int:
        graph = defaultdict(list)
        for s, d, w in edges:
            graph[s].append([d, w])
            graph[d].append([s, w])
        
        def findNearNodes(start):
            distances = [1e9]*n
            minHeap = [(0, start)]
            distances[start] = 0

            while minHeap:
                curr_dist, node = heappop(minHeap)
                for nd, dist in graph[node]:
                    new_dist = curr_dist + dist
                    if new_dist < distances[nd]:
                        heappush(minHeap, (new_dist, nd))
                        distances[nd] = new_dist
            return len([(i, val) for i, val in enumerate(distances) if val <=distanceThreshold and val != 0])
        
        city_num = 1e9
        best_city = 0
        for node in range(n):
            neighbour = findNearNodes(node)
            if  neighbour <= city_num:
                city_num =  neighbour
                best_city = node
        return best_city