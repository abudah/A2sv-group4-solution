class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        num_collections= defaultdict(int)
        for i in nums:
            num_collections[i] += 1
        heap = []
        for key, values in num_collections.items():
            heap.append((-values, key))
        heapify(heap)
        result = []
        for i in range(k):
            result.append(heappop(heap)[1])
        return result