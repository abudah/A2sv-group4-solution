num_vertices = int(input())

edges  = []



for col in range(num_vertices):
    row = list(map(int, input().split()))
    for r in range(len(row)):
        if row[r] == 1:
            if not (col, r) in  edges:
                edges.append((r, col))

print(len(edges))