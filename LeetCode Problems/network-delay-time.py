class Solution:
    def networkDelayTime(self, times: List[List[int]], n: int, k: int) -> int:
        distances = [1e9]*n
        graph = defaultdict(list)
        for s, d, t in times:
            graph[s].append([d, t])
        
        minheap = [(0, k)]
        distances[k - 1] = 0

        while minheap:
            curr_time, node = heappop(minheap)
            for neigh, time in graph[node]:
                new_time = curr_time + time
                if new_time < distances[neigh -1]:
                    distances[neigh - 1] = new_time
                    heappush(minheap, (new_time, neigh))

        return max(distances) if max(distances) != 1e9 else -1
            