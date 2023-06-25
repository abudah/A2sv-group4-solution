class Solution:
    def minimumOperations(self, nums: List[int]) -> int:
        minHeap = [i for i in nums if i != 0]
        answer = 0
        heapify(minHeap)
        while minHeap:
            last = heappop(minHeap)
            while minHeap and last == minHeap[0]:
                heappop(minHeap)
            answer += 1
        return answer
            