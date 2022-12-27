# Enter your code here. Read input from STDIN. Print output to STDOUT
sizes=[int(i) for i in input().split()]
arrayOfIntegers=[int(i) for i in input().split()]
setA=set(int(i) for i in input().split())
setB=set(int(i) for i in input().split())
happiness=0
for i in arrayOfIntegers:
    if i in setB:
        happiness-=1
    if i in setA:
        happiness+=1
print(happiness)