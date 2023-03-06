# Problem: B. Dragons
# Contest: Codeforces - A2SV (Remote) Contest #5
# URL: https://codeforces.com/gym/424233/problem/B
# Memory Limit: 256 MB
# Time Limit: 1000 ms
# 
# Powered by CP Editor (https://cpeditor.org)

from copy import deepcopy

def solve(s,dragons):
	dragons.sort()
	powerful=[]
	for i in dragons:
		if i[0]<s:
			s+=i[1]
		else:
			powerful.append(i)
	if powerful:
		return "NO"
	return "YES"
	


s,n=map(int,input().split())
dragons=[]
for i in range(n):
	power,bonus=map(int,input().split())
	dragons.append([power,bonus])
print(solve(s,dragons))