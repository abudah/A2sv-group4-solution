class Solution:
    def replaceElements(self, arr: List[int]) -> List[int]:
        curr,great=0,0
        max_=-1
        while curr<len(arr):
            if curr==great and curr+1<len(arr):
                max_=-1
                for i in range(curr+1,len(arr)):
                        if arr[i]>max_:
                            max_=arr[i]
                            great=i
            arr[curr]=max_       
            curr+=1     
        arr[-1]=-1
        return arr
