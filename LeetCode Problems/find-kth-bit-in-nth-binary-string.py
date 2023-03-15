class Solution:
    def invert(self,val):
        val=[i for i in val]
        for i in range(len(val)):
            if val[i]=="1":
                val[i]="0"
            else:
                val[i]="1"
        return "".join(val)

    def findIt(self,n):
        if n==1:
            return '0'
        prev=self.findIt(n-1)
        inverted=self.invert(prev)
        res=prev + "1" + inverted[::-1]
        return res
   
    def findKthBit(self, n: int, k: int) -> str:         
        result=self.findIt(n)
        return result[k-1]
    
