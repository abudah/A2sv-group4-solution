# Problem: G. Bear and Big Brother
# Contest: Codeforces - Contest 1
# URL: https://codeforces.com/group/jUHXVvhswc/contest/419850/problem/G
# Memory Limit: 256 MB
# Time Limit: 1000 ms
# 
# Powered by CP Editor (https://cpeditor.org)

limak,bob=map(int,input().split())

i=0

while limak<=bob:
	limak*=3
	bob*=2
	i+=1
print(i)