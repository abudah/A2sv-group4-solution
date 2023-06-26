class Solution:
    def findFinalValue(self, nums: List[int], original: int) -> int:
        dictionary = defaultdict(int)

        for j in nums:
            dictionary[j] += 1
        while original in dictionary:
            original *= 2
        return original