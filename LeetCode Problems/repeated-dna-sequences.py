class Solution:
    def findRepeatedDnaSequences(self, s: str) -> List[str]:
        patterns = defaultdict(int)
        repeated_patterns = set()

        i = 0
        while i < len(s) - 9:
            if s[i:i+10] in patterns:
                repeated_patterns.add(s[i:i+10])
            else:
                patterns[s[i:i+10]] = 1
            i += 1
        return repeated_patterns