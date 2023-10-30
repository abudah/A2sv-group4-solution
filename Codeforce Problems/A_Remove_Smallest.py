tc=int(input())
for i in range(tc):
    length=int(input())
    integers=[int(i) for i in input().split()]
    integers.sort()
    flag="YES"
    copyIntegers=integers
    for i in range(length-1):
        if integers[i]-integers[i+1]==1 or integers[i]-integers[i+1]==0 :
            continue
        else:
            flag="NO"
            break

    print(flag)
            