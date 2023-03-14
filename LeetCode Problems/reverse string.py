class Solution:
    def reverseString(self, s: List[str]) -> None:
        """
        Do not return anything, modify s in-place instead.
        """
        
        def swap(val,ind):
            s[ind]=s[-(ind+1)]
            s[-(ind+1)]=val
        for i in range(len(s)//2):
            swap(s[i],i)