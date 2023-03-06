# Problem: A. Next Round
# Contest: Codeforces - VK Cup 2012 Qualification Round 1
# URL: https://codeforces.com/problemset/problem/158/A
# Memory Limit: 256 MB
# Time Limit: 3000 ms
# 
# Powered by CP Editor (https://cpeditor.org)

contestant,target=[int(i) for i in input().split()]

scores=[int(i) for i in input().split()]

rank=target
if scores[target-1]==0:
		while scores[target-1]==0 and target>0:
			target-=1
		rank=target

if scores[target-1]>0 and contestant>target :
	while scores[target-1]==scores[target] :
		target+=1
		if contestant==target:
			break;
	rank=target
	
print(rank)
	


			