# Enter your code here. Read input from STDIN. Print output to STDOUT
from collections import defaultdict

inputs=[int(i) for i in input().split()]
listingA=defaultdict(list)
listingB=[]
for i in range(inputs[0]):
    a=input()
    listingA[a].append(str(i+1))

for j in range(inputs[1]):
    b=input()
    listingB.append(b)


for i in listingB:
    if i not in listingA:
        print(-1)
    else:
        print(" ".join(listingA[i]))