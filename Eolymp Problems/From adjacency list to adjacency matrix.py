num_vertices = int(input())

graph = [[0 for i in range(num_vertices)] for j in range(num_vertices)]


for col in range(num_vertices):
    neighbours = list(map(int, input().split()))
    for row in range(1, len(neighbours)):
        graph[col][neighbours[row]-1] = 1
for row in graph:
    print(' '.join(map(str, row)))