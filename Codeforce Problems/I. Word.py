# Problem: I. Word
# Contest: Codeforces - Contest 1
# URL: https://codeforces.com/group/jUHXVvhswc/contest/419850/problem/I
# Memory Limit: 256 MB
# Time Limit: 2000 ms
# 
# Powered by CP Editor (https://cpeditor.org)

word=input()

upper=sum(1 for c in word if c.isupper())
lower=sum(1 for c in word if c.islower())
if upper>lower:
	print(word.upper())
else:
	print(word.lower())