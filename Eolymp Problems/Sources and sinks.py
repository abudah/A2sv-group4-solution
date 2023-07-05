num_vertex = int(input())
graph = []


for i in range(num_vertex):
    rows = list(map(int, input().split()))
    graph.append(rows)
source = []
sink = []

for r in range(num_vertex):
    countSource = 0
    countSink = 0
    for c in range(num_vertex):
        countSink += graph[r][c]
        countSource += graph[c][r]
    if not countSource:
        source.append(r+1)
    if not countSink:
        sink.append(r+1)
print(len(source), *source)
print(len(sink), *sink)
