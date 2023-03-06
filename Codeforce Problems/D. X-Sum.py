# Problem: D. X-Sum
# Contest: Codeforces - Codeforces Round #790 (Div. 4)
# URL: https://codeforces.com/contest/1676/problem/D
# Memory Limit: 256 MB
# Time Limit: 2000 ms
# 
# Powered by CP Editor (https://cpeditor.org)
from collections import defaultdict
tc=int(input())

for i in range(tc):
	n,m=[int(i) for i in input().split()]
	matrix=[]
	for i in range(n):
		rows=[int(i) for i in input().split()]
		matrix.append(rows)
	left_diagonal=defaultdict(int)
	right_diagonal=defaultdict(int)
	for i in range(n):
		for j in range(m):
			left_diagonal[i-j]+=matrix[i][j]
			right_diagonal[i+j]+=matrix[i][j]
			
	maximal=0
	for i in range(n):
		for j in range(m):
			val=left_diagonal[i-j]+right_diagonal[i+j]-matrix[i][j]
			maximal=max(val,maximal)	
	print(maximal)	
											