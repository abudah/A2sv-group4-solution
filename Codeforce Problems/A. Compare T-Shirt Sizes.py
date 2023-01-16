from collections import Counter

testCases=int(input())

for i in range(testCases):
    sizes=[i for i in input().split()]
    first=sizes[0]
    second=sizes[1]
    judge=''
    if first[-1]=="S" and second[-1]=="M" :
        judge="<"
    elif first[-1]=="M" and second[-1]=="S":
        judge=">"
    elif first[-1]=="L" and second[-1]=="S":
        judge=">"
    elif first[-1]=="S" and second[-1]=="L":
        judge="<"
    elif first[-1]=="L" and second[-1]=="M":
        judge=">"    
    elif first[-1]=="M" and second[-1]=="L":
        judge="<"    
    elif first[-1]==second[-1]:
        if first[-1]=="S":
            if len(first)>len(second):
                 judge="<"
            elif len(first)<len(second):
                 judge=">"
            else:
                 judge="="
        else:
            if len(first)>len(second) and first[-1]!="S":
                 judge=">"
            elif len(first)<len(second):
                 judge="<"
            else:
                 judge="="

    print(judge)
