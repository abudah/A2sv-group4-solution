numOfCoins=int(input())
 
coins=[int(i) for i in input().split()]
coins.sort(reverse=True)
total=sum(coins)
forMe=0
numOfcoin=0
i=0
while forMe<=total/2:
    forMe+=coins[i]
    i+=1
print(i)
