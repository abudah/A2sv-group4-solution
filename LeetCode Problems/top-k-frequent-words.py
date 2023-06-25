class Solution:
    def topKFrequent(self, words: List[str], k: int) -> List[str]:
        count = Counter(words)
        heap = [(-val, key) for key, val in count.items()]

        heapify(heap)

        return [heappop(heap)[1] for i in range(k)]
        