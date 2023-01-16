class Solution:
    def findWinners(self, matches: List[List[int]]) -> List[List[int]]:
        scoreBoard={}
        for i in range(len(matches)):
            if matches[i][0] in scoreBoard:
                scoreBoard[matches[i][0]][0]+=1
                scoreBoard[matches[i][0]][1]+=1
            if matches[i][1] in scoreBoard:
                scoreBoard[matches[i][1]][2]+=1
                scoreBoard[matches[i][1]][1]+=1
            if matches[i][0] not in scoreBoard:
                scoreBoard[matches[i][0]]=[1,1,0]
            if matches[i][1] not in scoreBoard:
                scoreBoard[matches[i][1]]=[0,1,1]
        
        
        notLost=[]
        lostOnce=[]
        for key,value in scoreBoard.items():
            if value[0]==value[1]:
                notLost.append(key)
            if value[1]-value[0]==1:
                lostOnce.append(key)
        notLost.sort()
        lostOnce.sort()
        return [notLost,lostOnce]