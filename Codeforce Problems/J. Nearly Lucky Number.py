# Problem: J. Nearly Lucky Number
# Contest: Codeforces - Contest 1
# URL: https://codeforces.com/group/jUHXVvhswc/contest/419850/problem/J
# Memory Limit: 256 MB
# Time Limit: 2000 ms
# 
# Powered by CP Editor (https://cpeditor.org)

nums=input()
flag="YES"

for i in nums:
	if i not in ['4','7']:
		flag="NO"
		break
if '4' not in nums:
	flag="NO"
if '7' not in nums:
	flag="NO"
print(flag)