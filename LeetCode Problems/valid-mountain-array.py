class Solution:
    def validMountainArray(self, arr: List[int]) -> bool:
        top=max(arr)
        index=arr.index(top)
        if not index or index==len(arr)-1:
            return False
        for i in range(len(arr)-1):
            if i<index and arr[i] >=arr[i+1]:
                return False
            if i>=index and arr[i] <=arr[i+1]:
                return False
        return True
        

        