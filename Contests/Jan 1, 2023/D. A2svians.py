n=int(input())
members=[]
a=input().split()
bads=input().split()
excellents=0
for i in bads:
        a.remove(i)
for i in a:
        if len(set(i))==len(i) or len(set(i))==len(i)//2:
                excellents+=1

print(excellents)
        
