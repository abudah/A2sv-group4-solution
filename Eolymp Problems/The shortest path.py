from collections import defaultdict, deque

graph = defaultdict(set)

n, m = list(map(int, input().split()))
source, destination = list(map(int, input().split()))

for i in range(m):
    start, end = list(map(int, input().split()))
    graph[start].add(end)
    graph[end].add(start)

queue = deque([source])
path = {source:-1}


while queue:
    node = queue.popleft()
    if node == destination:
        break
    
    for neighbours in graph[node]:
        if neighbours not in path:
            path[neighbours] = node
            queue.append(neighbours)
            
if destination not in path:
    print(-1)
else:
    current = destination
    answer = []
    while current != -1:
        answer.append(current)
        current = path[current]
    print(len(answer)-1)
    print(' '.join(map(str, answer[::-1])))