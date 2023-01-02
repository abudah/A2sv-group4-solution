n=int(input())
on=[]
for i in range(n):
        args=input().split()
        colors=input()
        val=colors.index(args[1])
        colors+=colors
        curr=0
        distances=0
        nearest=0
        targetFound=False
        while(curr<len(colors)):
                if  colors[curr]==args[1]:
                        targetFound=True
                if  targetFound:
                        if colors[curr]=='g':
                                distances=max(distances,nearest)
                                nearest=0
                                targetFound=False
                        else:
                                nearest+=1
                curr+=1
        print(distances)

