class NumMatrix:

    def __init__(self, matrix: List[List[int]]):
        row,col=len(matrix),len(matrix[0])
        self.pref_sum=[[0]*(col+1) for i in range(row+1)]
        for r in range(row):
            pref=0
            for c in range(col):
                pref+=matrix[r][c]
                above=self.pref_sum[r][c+1]
                self.pref_sum[r+1][c+1]=pref+above
    
        
    def sumRegion(self, row1: int, col1: int, row2: int, col2: int) -> int:
        row1,col1,row2,col2=row1+1,col1+1,row2+1,col2+1

        return self.pref_sum[row2][col2]-self.pref_sum[row1-1][col2]-self.pref_sum[row2][col1-1]+self.pref_sum[row1-1][col1-1]
