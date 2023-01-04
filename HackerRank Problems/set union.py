# Enter your code here. Read input from STDIN. Print output to STDOUT
Eng=int(input())
EngRoleNumbers=set(int(i) for i in input().split())

Fre=int(input())
FreRoleNumbers=set(int(i) for i in input().split())

print(len(EngRoleNumbers.union(FreRoleNumbers)))
