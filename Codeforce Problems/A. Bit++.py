# Problem: A. Bit++
# Contest: Codeforces - Codeforces Round #173 (Div. 2)
# URL: https://codeforces.com/problemset/problem/282/A
# Memory Limit: 256 MB
# Time Limit: 1000 ms
# 
# Powered by CP Editor (https://cpeditor.org)

noOfStatements=int(input())

x=0

for i in range(noOfStatements):
	n=input()
	if n=='++X' or n=='X++':
		x+=1
	if n=="--X" or n=="X--":
		x-=1
print(x)