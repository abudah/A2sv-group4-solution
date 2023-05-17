from collections import defaultdict


num_vertices, num_edges = list(map(int, input().split()))

graph = defaultdict(list)
degree = [0 for i in range(num_vertices)]

for i in range(num_edges):
    source, destination = list(map(int, input().split()))

    graph[source].append(destination)
    graph[destination].append(source)
    degree[source-1] += 1 
    degree[destination-1] += 1


if len(set(degree)) <= 1:
    print("YES")
else:
    print("NO")