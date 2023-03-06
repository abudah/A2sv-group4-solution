class Solution:
    def pancakeSort(self, arr: List[int]) -> List[int]:
        def flip(end):
            start=0
            while start<end:
                arr[start],arr[end]=arr[end],arr[start]
                start+=1
                end-=1
        n=len(arr)
        result=[]
        for i in range(n-1,-1,-1):
            max_len=i
            for j in range(i,-1,-1):
                if arr[j]>arr[max_len]:
                    max_len=j
            if max_len!=i:
                flip(max_len)
                flip(i)
                result.append(max_len+1)
                result.append(i+1)
        return result