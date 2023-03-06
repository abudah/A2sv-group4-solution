class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        zeroLoc=set()
        for i in range(len(matrix)):
            for j in range(len(matrix[0])):
                if matrix[i][j]==0:
                    zeroLoc.add((i,j))
        for el in zeroLoc:
            for i in range(len(matrix[0])):
                matrix[el[0]][i]=0
            for j in range(len(matrix)):
                matrix[j][el[1]]=0