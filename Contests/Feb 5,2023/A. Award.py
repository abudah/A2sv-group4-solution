# Problem: A. Award
# Contest: Codeforces - A2SV (Remote) Contest #6
# URL: https://codeforces.com/gym/425122/problem/0
# Memory Limit: 256 MB
# Time Limit: 1000 ms
# 
# Powered by CP Editor (https://cpeditor.org)

participant,pen,notebook=[int(i) for i in input().split()]

for i in range(participant):
	pen-=1
	notebook-=1
if pen < 0 or notebook< 0:
	print("No")
else:
	print("Yes")