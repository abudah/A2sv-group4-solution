class Solution:
    def getRow(self, rowIndex: int) -> List[int]:
        if rowIndex==0:
            return [1]
        if rowIndex==1:
            return [1,1]
        A=[]
        b=self.getRow(rowIndex-1)
        for i in range(len(b)-1):
            A.append(b[i]+b[i+1])
        return [1]+A+[1]

        
        
        