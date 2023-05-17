from collections import defaultdict

num_vertices = int(input())

graph = defaultdict(list)

for col in range(1, num_vertices+1):
    row = list(map(int, input().split()))
    for r in range(1, len(row)+1):
        if row[r-1] == 1:
            graph[col].append(r)
for vertices in graph.values():
    print(str(len(vertices)) + " "+ ' '.join(map(str, vertices)))