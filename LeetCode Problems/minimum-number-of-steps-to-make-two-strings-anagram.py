class Solution:
    def minSteps(self, s: str, t: str) -> int:
        reference = defaultdict(int)
        for i in t:
            reference[i] += 1
        count = 0
        for j in s:
            if j in reference and reference[j] > 0:
                reference[j] -= 1
            else:
                count += 1
        return count