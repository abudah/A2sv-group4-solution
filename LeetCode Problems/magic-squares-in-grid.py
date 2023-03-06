class Solution:
    def numMagicSquaresInside(self, grid: List[List[int]]) -> int:
        """
        [[4,3,8,4],[9,5,1,9],[2,7,6,2]]
        case 1: if less than 3x3 return 0
        case 2: sliding window over it
            take all values into a list and check if they are distinict and full
            if they are count and then jump to the next sliding window
        approach to solution:
        


        """
        rowEnd,colEnd=3,3
        rowStart,colStart=0,0
        standard={1,2,3,4,5,6,7,8,9}
        count=0
        while rowEnd<=len(grid):
            minimal=[]
            distinict=set()
            for row in range(rowStart,rowEnd):
                mini=[]
                for col in range(colStart,colEnd):
                    mini.append(grid[row][col])
                    distinict.add(grid[row][col])
                    
                minimal.append(mini)
                
            if minimal[0][0]+minimal[1][1]+minimal[2][2]==minimal[0][2]+minimal[1][1]+minimal[2][0] ==sum(minimal[0]) ==sum(minimal[1])==sum(minimal[2])==minimal[1][0]+minimal[0][0]+minimal[2][0]==minimal[1][1]+minimal[0][1]+minimal[2][1]==minimal[0][2]+minimal[1][2]+minimal[2][2] and distinict==standard:
                count+=1
            if colEnd==len(grid[0]):
                colStart=0
                colEnd=3
                rowStart+=1
                rowEnd+=1
            else:
                colStart+=1
                colEnd+=1
           
        return count
