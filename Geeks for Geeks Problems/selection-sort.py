#User function Template for python3

class Solution: 
    def select(self, arr, i):
        minimumIndex=i
        for n in range(i+1,len(arr)):
                if arr[n]<arr[minimumIndex]:
                    minimumIndex=n
        return minimumIndex
        

    def selectionSort(self, arr,n):
        for i in range(len(arr)-1):
            minPos=self.select(arr,i)
            arr[i],arr[minPos]=arr[minPos],arr[i]
            


#{ 
 # Driver Code Starts
#Initial Template for Python 3

if __name__ == '__main__': 
    t = int(input())
    for _ in range(t):
        n = int(input())
        arr = list(map(int, input().strip().split()))
        Solution().selectionSort(arr, n)
        for i in range(n):
            print(arr[i],end=" ")
        print()
# } Driver Code Ends