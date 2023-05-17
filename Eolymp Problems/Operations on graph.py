from collections import defaultdict

num_vertices = int(input())

num_operations = int(input())

graph = defaultdict(list)


def add_edge(u, v):
    graph[u].append(v)
    graph[v].append(u)


for _ in range(num_operations):
    operation = list(map(int, input().split()))
    
    if operation[0] == 1:
        add_edge(operation[1], operation[2])
    if operation[0] == 2:
        if graph[operation[1]]:
            adjacents = ' '.join(map(str,graph[operation[1]]))
            print(adjacents)