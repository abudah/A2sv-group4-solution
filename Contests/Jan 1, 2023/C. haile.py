n=int(input())
datas=[]
for i in range(n):
    data=input()
    data=data.split('#')
    datas.append(' '.join(data))
for i in datas:
    print(i)
