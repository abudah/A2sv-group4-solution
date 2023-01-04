# Enter your code here. Read input from STDIN. Print output to STDOUT
engl=int(input())
engRols=set(int(i) for i in input().split())
Fr=int(input())
FreRols=set(int(i) for i in input().split())
print(len(engRols.difference(FreRols)))