# // Problem: A. Team
# // Contest: Codeforces - Codeforces Round #143 (Div. 2)
# // URL: https://codeforces.com/problemset/problem/231/A
# // Memory Limit: 256 MB
# // Time Limit: 2000 ms
# // 
# // Powered by CP Editor (https://cpeditor.org)

noOfProblems=int(input())

canSolve=0
for i in range(noOfProblems):
	problem=[int(i) for i in input().split()]
	if sum(problem)>1:
		canSolve+=1
print(canSolve)