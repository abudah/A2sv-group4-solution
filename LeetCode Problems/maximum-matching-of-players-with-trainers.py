class Solution:
    def matchPlayersAndTrainers(self, players: List[int], trainers: List[int]) -> int:
        players.sort()
        trainers.sort()
        count = 0
        prev = 0

        for i in players:
            while prev <= len(trainers)-1:
                if trainers[prev] >= i:
                    count +=1
                    prev +=1
                    break
                prev +=1
        return count
      