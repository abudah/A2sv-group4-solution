from collections import defaultdict, deque
import heapq

n, m = list(map(int, input().split()))

graph = defaultdict(list)
for _ in range(m):
    s, d, w = list(map(int, input().split()))
    graph[s].append([d, w])
    graph[d].append([s, w])
distances = [1e9] * n
distances[0] = 0
minHeap = [(0, 1)]
visited = set()
parents = [i for i in range(1, n + 1)]

while minHeap:
    curr_dist, node = heapq.heappop(minHeap)
    if node in visited:
        continue
    visited.add(node)
    for nd, w in graph[node]:
        new_dist = curr_dist + w
        if new_dist < distances[nd - 1]:
            distances[nd - 1] = new_dist
            heapq.heappush(minHeap, (new_dist, nd))
            parents[nd - 1] = node
        # if nd == n:
        #     paths.append(new_dist)
if distances[n - 1] == 1e9:
    print(-1)
    exit()
end = n
path = []
while parents[end - 1] != end:
    # print(node)
    path.append(end)
    end = parents[end - 1]
path.append(1)
path.reverse()

print(*path)


# Gives TlE on 28th Testcase due to too much constraint which is (2 ≤ n ≤ 1e5, 0 ≤ m ≤ 1e5),