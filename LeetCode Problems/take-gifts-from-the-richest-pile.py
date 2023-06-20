class Solution:
    def pickGifts(self, gifts: List[int], k: int) -> int:
        gift = [-i for i in gifts]
        heapq.heapify(gift)
        for i in range(k):
            w = int(sqrt(-heapq.heappop(gift)))
            heapq.heappush(gift, -w)
        return -sum(gift)