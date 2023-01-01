n=int(input())
on=[]
for i in range(n):
        args=input().split()
        colors=input()
        val=colors.index(args[1])
        on.append(colors.index('g'))
                        

for i in on:
        print(i)
