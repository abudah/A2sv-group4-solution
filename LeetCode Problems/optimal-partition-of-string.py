class Solution:
    def partitionString(self, s: str) -> int:
        chars = {}
        count = 0
        for i in s:
            if i in chars:
                count += 1
                chars.clear()
            chars[i] = 1
        if chars:
            count += 1
        return count