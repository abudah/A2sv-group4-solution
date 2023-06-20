class Solution:
    def kWeakestRows(self, mat: List[List[int]], k: int) -> List[int]:
        results = [(sum(el), i) for i,el in enumerate(mat)]

        heapq.heapify(results)
        answers = []
        for i in range(k):
            row, index = heapq.heappop(results)
            answers.append(index)
        return answers