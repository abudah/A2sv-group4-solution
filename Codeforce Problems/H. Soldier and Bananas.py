# Problem: H. Soldier and Bananas
# Contest: Codeforces - Contest 1
# URL: https://codeforces.com/group/jUHXVvhswc/contest/419850/problem/H
# Memory Limit: 256 MB
# Time Limit: 1000 ms
# 
# Powered by CP Editor (https://cpeditor.org)

inCost,initial,wants=map(int,input().split())

cost=0

for i in range(1,wants+1):
	cost+=i*inCost

if cost-initial<=0:
	print(0)
else:
	print(cost-initial)