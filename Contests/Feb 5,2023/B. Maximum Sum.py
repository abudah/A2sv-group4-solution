# Problem: B. Maximum Sum
# Contest: Codeforces - A2SV (Remote) Contest #6
# URL: https://codeforces.com/gym/425122/problem/B
# Memory Limit: 256 MB
# Time Limit: 1000 ms
# 
# Powered by CP Editor (https://cpeditor.org)


numbers,bobsCap=[int(i) for i in input().split()]

prices=[int(i) for i in input().split()]

prices.sort()

totalEarning=0

for j,i in enumerate(prices):
	if i<0 and j < bobsCap:
  		totalEarning+=abs(i)
	
print(totalEarning)
