# Enter your code here. Read input from STDIN. Print output to STDOUT
dict={}

n=int(input())
for i in range(n):
    word=input()
    if word in dict.keys():
        dict[word]+=1
    else:
        dict[word]=1
print(len(dict))
for i in dict.values():
    print(i,end=' ')