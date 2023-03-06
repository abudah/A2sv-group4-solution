krito,dragons=[int(i) for i in input().split()]
level=[]
flag="YES"
for i in range(dragons):
    dragon=[int(i) for i in input().split()]
    level.append(dragon)
for i in level:
    if i[0]<krito:
        krito=krito+i[1]
        continue
    else:
        flag="NO"
        break
print(flag)
