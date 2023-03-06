# Problem: A. Add Opposite Values
# Contest: Codeforces - A2SV (Remote) Contest #9
# URL: https://codeforces.com/gym/429357/problem/A
# Memory Limit: 256 MB
# Time Limit: 1000 ms
# 
# Powered by CP Editor (https://cpeditor.org)

tc=int(input())

for i in range(tc):
	length=int(input())
	original=0
	binary=input()
	left=0
	right=len(binary)-1
	while binary[left]!=binary[right] and left<right:
		left+=1
		right-=1
	print(right+1-left)
		
		
