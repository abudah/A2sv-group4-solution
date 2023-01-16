givens=[int(i) for i in input().split()]
lanterns=[int(i) for i in input().split()]
lanterns.sort()
d=0
for i in range(len(lanterns)-1):
        d=max(d,(lanterns[i+1]-lanterns[i])/2)
d=max(d,lanterns[0], givens[-1]-lanterns[-1])
print(d)
