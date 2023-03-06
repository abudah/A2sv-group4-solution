# Problem: A. Remove Smallest
# Contest: Codeforces - Codeforces Round #661 (Div. 3)
# URL: https://codeforces.com/problemset/problem/1399/A
# Memory Limit: 256 MB
# Time Limit: 1000 ms
# 
# Powered by CP Editor (https://cpeditor.org)

tc=int(input())

def checker(arr,length):
	for i in range(length-1):
		if arr[i+1]-arr[i]>1:
			return "NO"
	return "YES"
	
for i in range(tc):
	length=int(input())
	integers=[int(i) for i in input().split()]
	integers.sort()
	print(checker(integers,length))
