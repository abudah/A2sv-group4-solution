class Solution:
    def matrixReshape(self, mat: List[List[int]], r: int, c: int) -> List[List[int]]:
        data=[]
        for i in mat:
            data.extend(i)
        if r*c!=len(data):
            return mat
        newMat=[]
        for i in range(r):
            newMat.append(data[i*c:i*c+c])
        return newMat