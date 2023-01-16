n=int(input())
scores=[int(i) for i in input().split()]
first=scores[0]
fromUpper=first
fromLower=first
amazing=0



for i in range(1,n):
    if  scores[i]>fromUpper:
            amazing+=1
            fromUpper=scores[i]
    elif scores[i]< fromLower:
            amazing+=1
            fromLower=scores[i]
        
print(amazing)
