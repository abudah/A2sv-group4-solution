class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        j=0
        while j<len(matrix):
            if matrix[j][0] > target:
                break
            j+=1
        if target in matrix[j-1]:
            return True
        return False