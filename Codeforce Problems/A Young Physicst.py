n=int(input())

sums=[0,0,0]

for i in range(n):
        a=[int(i) for i in input().split()]
        sums[0]+=a[0]
        sums[1]+=a[1]
        sums[2]+=a[2]
if sums[0]!=0 or sums[1]!=0 or sums[2]!=0:
        print("NO")
else:
        print("YES")

        
