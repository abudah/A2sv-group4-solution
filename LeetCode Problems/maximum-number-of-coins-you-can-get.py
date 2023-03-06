class Solution:
    def maxCoins(self, piles: List[int]) -> int:
        piles.sort()
        myTurn=len(piles)-2
        bobsTurn=0
        total=0
        while myTurn>bobsTurn:
            total+=piles[myTurn]
            bobsTurn+=1
            myTurn-=2
        return total