# Enter your code here. Read input from STDIN. Print output to STDOUT
n=int(input())

roomNumbers=[int(i) for i in input().split()]

dict={}

for i in range(len(roomNumbers)):
    if roomNumbers[i] in dict.keys():
        dict[roomNumbers[i]]+=1
    else:
        dict[roomNumbers[i]]=1
for key,value in dict.items():
    if value!=n:
        print(key)
