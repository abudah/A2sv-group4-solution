import time
import os,sys
from datetime import datetime
from math import floor,sqrt,gcd,factorial,ceil
from collections import Counter,defaultdict
import bisect
from itertools import chain
from collections import deque
from sys import maxsize as INT_MAX
#import threading
'''Dont use setrecursionlimit in pypy'''
#sys.setrecursionlimit(int(1e9)+500)
#threading.stack_size(0x2000000)
ONLINE_JUDGE=False
if os.path.exists('D:\Contest'):
    ONLINE_JUDGE=True
INF=float('inf')
mod=int(1e9)+7
def readint():
    return int(sys.stdin.readline())
def readstr():
    return sys.stdin.readline()
def readlst():
    return list(map(int, sys.stdin.readline().strip().split()))
def readmul():
    return map(int, sys.stdin.readline().strip().split())
def mulfloat():
    return map(float, sys.stdin.readline().strip().split())
def flush():
    return sys.stdout.flush()
def power_two(x):
    return (1<<x)
def lcm(a,b):
    return a*b//gcd(a,b)
    
'''def ceil(a,b):
    return(int((a+b-1)/b))'''
 
def countGreater(arr,n, k):
    l = 0
    r = n - 1
    leftGreater = n
    while (l <= r):
        m = int(l + (r - l) / 2)
        if (arr[m] >= k):
            leftGreater = m
            r = m - 1
        else:
            l = m + 1
            return (n - leftGreater)
 
def two_pointer(n,val,*arr):
    l,r,cnt=0,n-1,0
    while l<r:
        if arr[l]+arr[r]>val:
            r-=1
        else:
            cnt+=r-l
            l+=1
    return cnt
 
def lower(arr,n,val):
    l,r=-1,n
    while r>l+1:
        m=int((l+r)>>1)
        if arr[m]<val:
            l=m
        else:
            r=m
    return r
 
def upper(arr,n,val):
    l,r=-1,n
    while r>l+1:
        m=int((l+r)>>1)
        if arr[m]<=val:
            l=m
        else:
 
            r=m
    return l
def BFS(adj, src, dist, paths, n):
    visited = [False] * n
    dist[src] = 0
    paths[src] = 1
    q = deque()
    q.append(src)
    visited[src] = True
    while q:
        curr = q[0]
        #print('q at start',q)
        q.popleft()
        for x in adj[curr]:
            #print('x',x)
            if not visited[x]:
                q.append(x)
                #print('q after append',q)
                visited[x] = True
            if dist[x] > dist[curr] + 1:
                dist[x] = dist[curr] + 1
                paths[x] = (paths[curr])%mod
            elif dist[x] == dist[curr] + 1:
                paths[x] =(paths[x]%mod+paths[curr]%mod)%mod
 
def binpow(a,n,mod):
    res=1
    while n:
        if n&1:
            res=(res*a)%mod
            n-=1
        a=(a*a)%mod
        n=n>>1
    return res
 
def is_perfect_square(num):
    #print(num)
    temp = num**(0.5)
    #print(temp)
    return (temp//1)==temp
def printmat(l):
    for i in range(0,len(l)):
        print(*l[i],sep="")
    print()
    
'''
c-space = to copy
o-space= to open file
,-space=to run prog
:noh= to get rid of text highlight
 
1. Implement after understanding properly don't do in vain.
2. Check corner cases.
3. Use python if there is recursion,try-catch,dictionary.
4. Use pypy if heavy loop,list slice.
'''
 
    
def john_3_16():
    n,m=readmul()
    a=readlst()
    b=readlst()
    d={}
    for i in a:
        try:
            d[i]+=1
        except:
            d[i]=1
    cnt=0
    for i in b:
        try:
            cnt+=d[i]
        except:
            continue
    print(cnt)
    return
def main():
    #tc=readint()
    tc=1
    start=time.time()
    while tc:
        john_3_16()
        tc-=1
    if ONLINE_JUDGE:
        print(f'{(time.time()-start)*1000}ms')
main()