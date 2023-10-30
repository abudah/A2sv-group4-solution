from collections import defaultdict, deque
import heapq

n, m = list(map(int, input().split()))

graph = defaultdict(list)
for _ in range(m):
    s, d = list(map(int, input().split()))
    graph[s].append(d)
    graph[d].append(s)
distances = [1e9] * n
minHeap = [(0, 0)]
visited = set()
paths = []

while minHeap:
    curr_dist, node = heapq.heappop(minHeap)
    if node in visited:
        continue
    visited.add(node)
    for nd in graph[node + 1]:
        new_dist = curr_dist + 1
        if new_dist < distances[nd - 1]:
            distances[nd - 1] = new_dist
            heapq.heappush(minHeap, (new_dist, nd - 1))
        if nd == n:
            paths.append(new_dist)
print(paths)
