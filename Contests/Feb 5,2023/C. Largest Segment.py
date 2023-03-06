# Problem: C. Largest Segment
# Contest: Codeforces - A2SV (Remote) Contest #6
# URL: https://codeforces.com/gym/425122/problem/C
# Memory Limit: 256 MB
# Time Limit: 2000 ms
# 
# Powered by CP Editor (https://cpeditor.org)

numOfSegments=int(input())
segments=[]

for i in range(numOfSegments):
	first,last=[int(i) for i in input().split()]
	segments.append([first,last])
	
first=sorted(segments)
second=sorted(segments,key=lambda x:x[1], reverse=True)

start=first[0][0]
end=second[0][1]

if [start,end] in segments:
	print(segments.index([start,end])+1)
else:
	print(-1)