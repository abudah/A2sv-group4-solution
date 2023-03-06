from collections import defaultdict
import math
class Solution:
    def equalPairs(self, grid: List[List[int]]) -> int:
        grids=[]
        listing=defaultdict(lambda : [0,0])
        for i in range(len(grid)):
            row=[]
            column=[]
            for j in range(len(grid)):
                row.append(grid[i][j])
                column.append(grid[j][i])
            listing[str(row)][0]+=1
            listing[str(column)][1]+=1
        pairNums=0
        for i in listing.values():
                pairNums+=math.prod(i)
        print(listing)
        return pairNums