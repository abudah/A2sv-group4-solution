class Solution:
    def findRelativeRanks(self, score: List[int]) -> List[str]:
        winners = ["Gold Medal", "Silver Medal","Bronze Medal"]
        heap = []
        for pos, scor in enumerate(score):
            heappush(heap, (-scor, pos))
        scoreboard = [0 for i in range(len(score))]
        i = 0
        while heap and i < 3:
            rank = heappop(heap)
            scoreboard[rank[1]] = winners[i]
            i += 1
        j = 3
        while heap:
            rank = heappop(heap)
            scoreboard[rank[1]] = str(j+1)
            j += 1
        return scoreboard